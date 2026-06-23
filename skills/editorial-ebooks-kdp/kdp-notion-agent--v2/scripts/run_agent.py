from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from docx_renderer import render_markdown_docx
from notion_client import DEFAULT_CORRECTED_PROPERTY, NotionClient, NotionConfig
from package_builder import build_final_package, count_words, resolve_package_title, validate_workspace


DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "kdp-agent"
DEFAULT_SOURCE_PROPERTY = "AUTO"
DEFAULT_EXECUTION_PROFILE = "premium"
SUPPORTED_PROFILES = {"premium", "economico"}
CRITICAL_SYNC_FILES = [
    "SKILL.md",
    "scripts/run_agent.py",
    "scripts/docx_renderer.py",
    "references/model-routing-policy.json",
]
PTBR_UNICODE_GUARDRAIL = (
    "REGRA CRÍTICA DE ENCODING E IDIOMA: escreva em português do Brasil natural preservando integralmente "
    "acentos e caracteres especiais reais em Unicode/UTF-8. Nunca translitere nem remova caracteres como "
    "á, à, ã, â, é, ê, í, ó, ô, õ, ú, ç. Exemplos proibidos: 'nao', 'sermao', 'capitulo', 'introducao', "
    "'conclusao', 'voce', 'coracao', 'oracao', 'bencao', 'fisico', 'fsico', 'correcao', 'correo' "
    "quando a forma correta exigir acento, cedilha ou letras completas. "
    "Se receber contexto sem acentos, normalize a saída final para o português correto."
)
BIBLICAL_TEXT_GUARDRAIL = (
    "REGRA CRÍTICA DE FIDELIDADE BÍBLICA: o ebook deve interagir continuamente com o texto bíblico de origem. "
    "Não escreva como se fossem apenas reflexões soltas do autor. Cada capítulo precisa nascer do texto base, "
    "explicar, aplicar ou desdobrar legitimamente sua mensagem, mantendo conexão visível com a passagem bíblica, "
    "seus movimentos, imagens, tensões e implicações pastorais."
)
PERSUASIVE_EBOOK_GUARDRAIL = (
    "REGRA CRÃTICA DE PADRÃƒO EDITORIAL: o ebook deve seguir obrigatoriamente a forma de escrever, o tom, a voz, "
    "a arquitetura, a progressÃ£o argumentativa e a lÃ³gica persuasiva da skill `generate-persuasive-ebooks`, "
    "especialmente no padrÃ£o cristÃ£o dos modelos aprovados pelo usuÃ¡rio. Isso inclui: introduÃ§Ã£o confessional, "
    "aberturas com cena/pergunta/tensÃ£o reconhecÃ­vel, cadÃªncia dor -> diagnÃ³stico -> revelaÃ§Ã£o -> prÃ¡tica -> esperanÃ§a, "
    "integraÃ§Ã£o orgÃ¢nica entre BÃ­blia, psicologia e aplicaÃ§Ã£o cotidiana, tÃ­tulos memorÃ¡veis, ritmo de livro e "
    "reposicionamento de identidade do leitor. NÃ£o copiar trechos literais; reproduzir o padrÃ£o editorial."
)

FIXED_PERSUASIVE_CHAPTER_ARCHITECTURE = (
    "ARQUITETURA FIXA POR CAPITULO (salvo limitacao real do sermao, que deve ser justificada):\n"
    "- Capitulo 1: identificacao profunda + dor latente + loop mental aberto. Nao entregue a solucao ainda.\n"
    "- Capitulo 2: causa raiz + quebra de crencas + momento AHA. O leitor precisa sentir 'agora tudo faz sentido'.\n"
    "- Capitulo 3: virada cognitiva + reposicionamento de identidade + caminho inicial de acao.\n"
    "- Capitulo 4: aprofundamento biblico e emocional da nova lente, consolidando a mudanca de percepcao.\n"
    "- Capitulo 5: 'O que a Biblia realmente diz', com explicacao clara do texto e correcao de leituras erradas.\n"
    "- Capitulo 6: framework pratico numerado, simples, executavel e pastoral.\n"
    "- Capitulo 7: aplicacao especifica para membros, lideres e pastores.\n"
    "- Capitulo 8: custo de continuar igual + esperanca pastoral + convite implicito a agir agora.\n\n"
    "Durante toda a escrita, ativar simultaneamente:\n"
    "- Reptiliano: seguranca vs risco, ganho vs perda, urgencia implicita, status e consequencia.\n"
    "- Limbico: historia plausivel, conflito interno, pertencimento, frustracao silenciosa, alivio e esperanca.\n"
    "- Neocortex: explicacao clara, estrutura organizada, causa -> efeito -> solucao, racionalidade depois do impacto emocional."
)


def persuasive_blueprint_scaffold(title: str) -> str:
    return (
        f"# Blueprint do Ebook: {title}\n\n"
        "## Promessa central\n\n"
        "## Leitor ideal\n\n"
        "## Titulo recomendado\n\n"
        "## Outras opcoes de titulo com justificativa\n\n"
        "## Subtitulo recomendado\n\n"
        "## Arco editorial obrigatorio\n\n"
        "- Hook:\n"
        "- Tensao:\n"
        "- Revelacao:\n"
        "- Transformacao:\n\n"
        "## Justificativa de aderencia ao padrao persuasive ebooks\n\n"
        "## Desvios estruturais justificados pelo sermao\n\n"
        "## Sumario proposto\n\n"
        "### Capitulo 1\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: identificacao profunda + dor latente + loop aberto\n"
        "- Crenca ou leitura defeituosa a expor:\n"
        "- Dor latente a amplificar:\n"
        "- Nova percepcao a preparar:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 2\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: causa raiz + quebra de crencas + momento AHA\n"
        "- Crenca ou leitura defeituosa a quebrar:\n"
        "- Dor latente a amplificar:\n"
        "- Novo modelo mental:\n"
        "- Analogia principal:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 3\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: virada cognitiva + reposicionamento de identidade + primeira acao\n"
        "- Crenca ou leitura defeituosa a substituir:\n"
        "- Dor latente a amplificar:\n"
        "- Nova identidade proposta:\n"
        "- Caminho claro apresentado:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 4\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: aprofundamento biblico e emocional da nova lente\n"
        "- Crenca ou leitura defeituosa a desmontar:\n"
        "- Dor latente a amplificar:\n"
        "- Nova identidade ou lente consolidada:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 5\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: o que a Biblia realmente diz\n"
        "- Leitura errada a corrigir:\n"
        "- Texto biblico central e explicacao:\n"
        "- Implicacao pastoral:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 6\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: framework pratico numerado\n"
        "- Bloqueio pratico a vencer:\n"
        "- Passos numerados:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 7\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: aplicacao para membros, lideres e pastores\n"
        "- Risco pastoral a evitar:\n"
        "- Aplicacao para membros:\n"
        "- Aplicacao para lideres:\n"
        "- Aplicacao para pastores:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Transicao para o proximo capitulo:\n\n"
        "### Capitulo 8\n\n"
        "- Objetivo neuroemocional:\n"
        "- Papel fixo no arco: custo de continuar igual + convite implicito a agir\n"
        "- Custo invisivel de permanecer igual:\n"
        "- Esperanca pastoral oferecida:\n"
        "- Pratica concreta imediata:\n"
        "- Ancora biblica:\n"
        "- Trecho do sermao que ancora:\n"
        "- Ganho do leitor ao final:\n"
        "- Fechamento e chamada implicita:\n"
    )


def chapter_role_spec(chapter_name: str) -> str:
    match = re.search(r"(\d+)", chapter_name)
    index = int(match.group(1)) if match else 0
    mapping = {
        1: (
            "Capitulo 1 - O desconforto que voce nao consegue explicar. Objetivo: gerar identificacao profunda "
            "+ abrir loop mental. Comecar com cena, pensamento comum ou tensao reconhecivel; nomear conflito "
            "interno invisivel; expor problema sentido mas pouco articulado; criar tensao crescente; fechar com "
            "pergunta ou quebra de expectativa. Nao entregar a solucao ainda."
        ),
        2: (
            "Capitulo 2 - A verdade que ninguem te explicou. Objetivo: revelar causa raiz + gerar momento AHA. "
            "Apresentar causa oculta do problema; quebrar crencas comuns; mostrar por que tentativas anteriores "
            "falharam; introduzir novo modelo mental; usar analogias simples e poderosas. Aqui acontece a virada cognitiva."
        ),
        3: (
            "Capitulo 3 - A virada que muda o jogo. Objetivo: reposicionar identidade + conduzir a acao. "
            "Mostrar o que muda quando o leitor entende a nova logica; apresentar caminho claro; reforcar o custo "
            "invisivel de continuar igual; criar senso de oportunidade acessivel agora; finalizar com convite implicito a agir."
        ),
        4: (
            "Capitulo 4 - Consolidacao da nova lente. Objetivo: aprofundar biblica e emocionalmente o novo modelo. "
            "Expandir a interpretacao correta com densidade pastoral; mostrar como a nova lente muda percepcao, afeto e pratica."
        ),
        5: (
            "Capitulo 5 - O que a Biblia realmente diz. Objetivo: corrigir leituras erradas e expor o texto biblico com clareza. "
            "O argumento precisa nascer do texto, nao de opinioes anexadas a ele."
        ),
        6: (
            "Capitulo 6 - Caminho pratico. Objetivo: transformar revelacao em framework numerado, simples e executavel. "
            "Organizar passos claros sem virar checklist seco."
        ),
        7: (
            "Capitulo 7 - Aplicacoes por responsabilidade. Objetivo: aplicar a verdade para membros, lideres e pastores. "
            "Ajustar a mesma tese para papeis diferentes sem perder unidade."
        ),
        8: (
            "Capitulo 8 - Decisao e fechamento. Objetivo: mostrar o custo de continuar igual, reposicionar a esperanca e "
            "encerrar com convite implicito a uma decisao concreta, sem parecer venda direta."
        ),
    }
    return mapping.get(
        index,
        "Capitulo fora da arquitetura preferencial. Justifique no blueprint por que o sermao exigiu esse desvio e preserve o arco hook -> tensao -> revelacao -> transformacao.",
    )


def main() -> int:
    _configure_stdio()
    parser = build_parser()
    args = parser.parse_args()
    warn_version_drift()

    if args.command == "inspect":
        client = NotionClient(NotionConfig.from_env())
        print(json.dumps(client.inspect_schema(), ensure_ascii=False, indent=2))
        return 0

    if args.command == "pull":
        client = NotionClient(NotionConfig.from_env())
        workspace = prepare_workspace(
            client,
            page_id=args.page_id,
            workspace_root=Path(args.workspace_root),
            source_property=args.source_property,
            execution_profile=args.profile,
            optional_artifacts=parse_artifacts_flag(args.artifacts),
        )
        print(workspace)
        return 0

    if args.command == "pull-next":
        client = NotionClient(NotionConfig.from_env())
        selection = select_next_eligible_page(
            client,
            title_query=args.title_contains,
            workspace_root=Path(args.workspace_root),
        )
        workspace = prepare_workspace(
            client,
            page_id=selection["page_id"],
            workspace_root=Path(args.workspace_root),
            source_property=args.source_property,
            execution_profile=args.profile,
            optional_artifacts=parse_artifacts_flag(args.artifacts),
        )
        print(json.dumps({**selection, "workspace": str(workspace)}, ensure_ascii=False, indent=2))
        return 0

    if args.command == "validate":
        issues = validate_workspace(Path(args.workspace), min_words=args.min_words)
        if issues:
            for issue in issues:
                print(f"- {issue}")
            return 1
        print("Workspace válido.")
        return 0

    if args.command == "prepare-stage-strategy":
        strategy_path = prepare_stage_strategy(Path(args.workspace))
        print(strategy_path)
        return 0

    if args.command == "prepare-model-routing":
        routing_path = prepare_model_routing(Path(args.workspace), profile=args.profile)
        print(routing_path)
        return 0

    if args.command == "prepare-codex-orchestration":
        orchestration_path = prepare_codex_orchestration(Path(args.workspace), profile=args.profile)
        print(orchestration_path)
        return 0

    if args.command == "prepare-cta-subagent":
        brief_path = prepare_cta_subagent_brief(Path(args.workspace))
        print(brief_path)
        return 0

    if args.command == "consolidate-chapters":
        ebook_path = consolidate_chapters(Path(args.workspace))
        print(f"Capítulos consolidados em {ebook_path}")
        return 0

    if args.command == "consolidate-cta-subagent":
        package = build_final_package(Path(args.workspace))
        report = promote_cta_subagent_output(
            package.files["cta_subagent"],
            package.files["cta_report"],
            title=package.metadata["title"],
        )
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    if args.command == "prepare-chapter-packet":
        packet_path = prepare_chapter_packet(Path(args.workspace), chapter_name=args.chapter)
        print(packet_path)
        return 0

    if args.command == "route-stage":
        route = route_stage(Path(args.workspace), stage=args.stage, chapter_name=args.chapter, profile=args.profile)
        print(json.dumps(route, ensure_ascii=False, indent=2))
        return 0

    if args.command == "run-editorial-stage":
        job_path = run_editorial_stage(
            Path(args.workspace),
            stage=args.stage,
            chapter_name=args.chapter,
            profile=args.profile,
            feedback=args.feedback,
        )
        print(job_path)
        return 0

    if args.command == "runs":
        report = list_runs(Path(args.workspace_root), page_id=args.page_id, limit=args.limit)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    if args.command == "healthcheck":
        issues = run_healthcheck()
        if issues:
            for issue in issues:
                print(f"- {issue}")
            return 1
        print("Healthcheck OK.")
        return 0

    if args.command == "sync-skills":
        result = sync_skills()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if args.command == "rollback-sync":
        result = rollback_sync(args.backup_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if args.command == "render":
        render_package(Path(args.workspace), min_words=args.min_words)
        print("Artefatos DOCX gerados.")
        return 0

    if args.command == "push":
        client = NotionClient(NotionConfig.from_env())
        push_package(client, Path(args.workspace), draft_status=args.draft_status)
        print("Pacote publicado como rascunho revisável.")
        return 0

    raise SystemExit(f"Comando não suportado: {args.command}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Orquestra o fluxo determinístico do KDP Notion Agent.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("inspect", help="Inspeciona o schema do banco Notion.")

    _artifacts_help = (
        "Artefatos opcionais a gerar: landing, bonus, metadata, cta (separados por vírgula). "
        "Use 'all' para todos ou 'none' para nenhum. Padrão: all."
    )
    pull = sub.add_parser("pull", help="Baixa uma página e prepara o workspace do caso.")
    pull.add_argument("--page-id", required=True)
    pull.add_argument("--workspace-root", default=str(DEFAULT_OUTPUT_DIR))
    pull.add_argument("--source-property", default=DEFAULT_SOURCE_PROPERTY)
    pull.add_argument("--profile", default=DEFAULT_EXECUTION_PROFILE, choices=sorted(SUPPORTED_PROFILES))
    pull.add_argument("--artifacts", default="all", help=_artifacts_help)

    pull_next = sub.add_parser("pull-next", help="Seleciona o próximo sermão elegível no Notion e prepara o workspace.")
    pull_next.add_argument("--workspace-root", default=str(DEFAULT_OUTPUT_DIR))
    pull_next.add_argument("--source-property", default=DEFAULT_SOURCE_PROPERTY)
    pull_next.add_argument("--title-contains")
    pull_next.add_argument("--profile", default=DEFAULT_EXECUTION_PROFILE, choices=sorted(SUPPORTED_PROFILES))
    pull_next.add_argument("--artifacts", default="all", help=_artifacts_help)

    validate = sub.add_parser("validate", help="Valida artefatos obrigatórios do workspace.")
    validate.add_argument("--workspace", required=True)
    validate.add_argument("--min-words", type=int, default=15000)

    prepare_strategy = sub.add_parser("prepare-stage-strategy", help="Gera a estrategia de economia de tokens por etapa.")
    prepare_strategy.add_argument("--workspace", required=True)

    prepare_routing = sub.add_parser("prepare-model-routing", help="Gera o plano autonomo de modelos por etapa.")
    prepare_routing.add_argument("--workspace", required=True)
    prepare_routing.add_argument("--profile", default=None, choices=sorted(SUPPORTED_PROFILES))

    prepare_codex = sub.add_parser("prepare-codex-orchestration", help="Gera o plano operacional do Codex com subagentes fixos por etapa.")
    prepare_codex.add_argument("--workspace", required=True)
    prepare_codex.add_argument("--profile", default=None, choices=sorted(SUPPORTED_PROFILES))

    render = sub.add_parser("render", help="Gera DOCX a partir do markdown do ebook e do bônus.")
    prepare_cta = sub.add_parser("prepare-cta-subagent", help="Gera um briefing formal para o subagente de CTA/coerencia.")
    prepare_cta.add_argument("--workspace", required=True)

    consolidate_chapters_cmd = sub.add_parser("consolidate-chapters", help="Mescla os rascunhos de chapter-drafts/ no 06_ebook.md preservando a ordem do blueprint.")
    consolidate_chapters_cmd.add_argument("--workspace", required=True)
    consolidate_cta = sub.add_parser("consolidate-cta-subagent", help="Promove o resultado do subagente para o relatorio CTA principal.")
    consolidate_cta.add_argument("--workspace", required=True)

    chapter_packet = sub.add_parser("prepare-chapter-packet", help="Gera um pacote enxuto de contexto para um capitulo.")
    chapter_packet.add_argument("--workspace", required=True)
    chapter_packet.add_argument("--chapter", required=True)

    route_stage_cmd = sub.add_parser("route-stage", help="Escolhe automaticamente modelo e contexto para uma etapa.")
    route_stage_cmd.add_argument("--workspace", required=True)
    route_stage_cmd.add_argument("--stage", required=True)
    route_stage_cmd.add_argument("--chapter")
    route_stage_cmd.add_argument("--profile", default=None, choices=sorted(SUPPORTED_PROFILES))

    run_stage_cmd = sub.add_parser("run-editorial-stage", help="Gera um job operacional completo para executar uma etapa editorial.")
    run_stage_cmd.add_argument("--workspace", required=True)
    run_stage_cmd.add_argument("--stage", required=True)
    run_stage_cmd.add_argument("--chapter")
    run_stage_cmd.add_argument("--profile", default=None, choices=sorted(SUPPORTED_PROFILES))
    run_stage_cmd.add_argument("--feedback")

    render.add_argument("--workspace", required=True)
    render.add_argument("--min-words", type=int, default=15000)

    push = sub.add_parser("push", help="Envia arquivos e propriedades para o Notion.")
    push.add_argument("--workspace", required=True)
    push.add_argument("--draft-status", default="Rascunho revisável")

    runs_cmd = sub.add_parser("runs", help="Lista histórico de execuções locais.")
    runs_cmd.add_argument("--workspace-root", default=str(DEFAULT_OUTPUT_DIR))
    runs_cmd.add_argument("--page-id")
    runs_cmd.add_argument("--limit", type=int, default=20)

    sub.add_parser("healthcheck", help="Valida consistência operacional da skill.")
    sub.add_parser("sync-skills", help="Sincroniza a skill com instalações locais e gera relatório.")

    rollback_cmd = sub.add_parser("rollback-sync", help="Restaura a última sincronização a partir de backup.")
    rollback_cmd.add_argument("--backup-id")
    return parser


def prepare_workspace(
    client: NotionClient,
    *,
    page_id: str,
    workspace_root: Path,
    source_property: str,
    execution_profile: str,
    optional_artifacts: list[str] | None = None,
) -> Path:
    client.ensure_status_property()
    page = client.get_page(page_id)
    title = client.extract_title(page)
    source_property = client.select_editorial_source(page, requested_property=source_property)
    source_file_name, raw_text = client.download_first_file(page, source_property)
    workspace = workspace_root / f"{safe_slug(title)}-{page_id[:8]}"
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "output").mkdir(exist_ok=True)
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:6]
    enabled = optional_artifacts if optional_artifacts is not None else sorted(_ALL_ARTIFACT_KEYS)
    client.write_manifest(
        workspace,
        page,
        source_property=source_property,
        source_file_name=source_file_name,
        execution_profile=execution_profile,
        run_id=run_id,
        optional_artifacts=enabled,
    )
    client.set_page_workflow_status(page_id, "Executando")
    write_default_files(workspace, title=title, raw_text=raw_text, source_property=source_property)
    return workspace


def select_next_eligible_page(
    client: NotionClient,
    *,
    title_query: str | None = None,
    workspace_root: Path | None = None,
) -> dict[str, Any]:
    eligible: list[dict[str, Any]] = []
    rejection_reasons: list[str] = []

    for page in client.list_database_pages():
        if not client.page_matches_title(page, title_query):
            continue
        is_eligible, reason = client.is_page_eligible_for_next_ebook(page)
        if not is_eligible:
            rejection_reasons.append(reason)
            continue
        title = client.extract_title(page)
        if workspace_root and workspace_exists_for_page(workspace_root, title=title, page_id=page["id"]):
            rejection_reasons.append(f"{title}: já possui workspace local preparado em {workspace_root}.")
            continue
        page_date = client.extract_page_date(page)
        eligible.append(
            {
                "page_id": page["id"],
                "title": title,
                "date": page_date.isoformat() if page_date else None,
                "source_property": client.select_editorial_source(page, requested_property="AUTO"),
                "reason": reason if not workspace_root else f"{reason} Sem workspace local prévio.",
            }
        )

    if not eligible:
        details = "\n- ".join(rejection_reasons[:10]) if rejection_reasons else "nenhuma página elegível encontrada."
        raise RuntimeError("Nenhum sermão elegível foi encontrado no Notion.\n- " + details)

    eligible.sort(key=lambda item: ((item["date"] or "9999-12-31"), item["title"].casefold()))
    return eligible[0]


def workspace_exists_for_page(workspace_root: Path, *, title: str, page_id: str) -> bool:
    ws = workspace_root / f"{safe_slug(title)}-{page_id[:8]}"
    return ws.is_dir() and (ws / "manifest.json").exists()


_ALL_ARTIFACT_KEYS = frozenset({"landing", "bonus", "metadata", "cta"})
_ARTIFACT_KEY_MAP = {
    "landing": "landing_html",
    "bonus": "bonus_markdown",
    "metadata": "kdp_metadata",
    "cta": "cta_report",
}
_ARTIFACT_STAGE_MAP = {
    "landing": "landing_page",
    "bonus": "bonus_asset",
    "metadata": "metadata_kdp",
    "cta": "cta_subagent",
}


def parse_artifacts_flag(value: str) -> list[str]:
    """Parse --artifacts flag into list of enabled artifact keys. Returns full list for 'all', empty for 'none'."""
    v = value.strip().lower()
    if v == "all":
        return sorted(_ALL_ARTIFACT_KEYS)
    if v == "none":
        return []
    keys = [k.strip() for k in v.split(",") if k.strip()]
    invalid = [k for k in keys if k not in _ALL_ARTIFACT_KEYS]
    if invalid:
        raise ValueError(f"Artefatos inválidos: {invalid}. Válidos: {sorted(_ALL_ARTIFACT_KEYS)}")
    return keys


def get_enabled_artifacts(workspace: Path) -> list[str]:
    """Read optional_artifacts from manifest. Returns all keys if field absent (backward compat)."""
    try:
        manifest = json.loads((workspace / "manifest.json").read_text(encoding="utf-8-sig"))
        artifacts = manifest.get("optional_artifacts")
        if artifacts is None:
            return sorted(_ALL_ARTIFACT_KEYS)
        return list(artifacts)
    except Exception:
        return sorted(_ALL_ARTIFACT_KEYS)


def write_default_files(workspace: Path, *, title: str, raw_text: str, source_property: str) -> None:
    manifest = json.loads((workspace / "manifest.json").read_text(encoding="utf-8-sig"))
    files = manifest["files"]
    enabled = set(manifest.get("optional_artifacts") or sorted(_ALL_ARTIFACT_KEYS))
    (workspace / files["raw_transcription"]).write_text(raw_text, encoding="utf-8")
    corrected_seed = raw_text if source_property == DEFAULT_CORRECTED_PROPERTY else ""
    _write_if_missing(workspace / files["corrected_transcription"], corrected_seed)
    _write_if_missing(
        workspace / files["sermon_summary"],
        (
            "# Resumo do Sermão\n\n"
            "## Tese central\n\n"
            "## Texto bíblico principal\n\n"
            "## Movimentos do argumento\n\n"
            "## Aplicações já presentes\n\n"
            "## Limites e riscos de extrapolação\n"
        ),
    )
    _write_if_missing(
        workspace / files["ebook_blueprint"],
        persuasive_blueprint_scaffold(title),
    )
    _write_if_missing(
        workspace / files["editorial_report"],
        (
            "# Relatório Editorial\n\n"
            "## Correções da transcrição\n\n"
            "## Principais decisões de adaptação\n\n"
            "## Gates de qualidade\n\n"
            "## Pendências ou riscos\n"
        ),
    )
    _write_if_missing(
        workspace / files["ebook_markdown"],
        (
            f"# {title}\n\n"
            "## Prefácio\n\n"
            "## Introdução\n\n"
            "## Capítulo 1\n\n"
            "## Capítulo 2\n\n"
            "## Conclusão\n"
        ),
    )
    if "landing" in enabled:
        _write_if_missing(workspace / files["landing_html"], "<!DOCTYPE html>\n<html lang=\"pt-BR\">\n<body>\n</body>\n</html>\n")
    if "bonus" in enabled:
        _write_if_missing(workspace / files["bonus_markdown"], f"# Bônus de {title}\n\n## Dia 1\n")
    if "metadata" in enabled:
        _write_if_missing(
            workspace / files["kdp_metadata"],
            json.dumps(
                {
                    "titulo": title,
                    "subtitulo": "",
                    "autor": "Filipe Ivo Pereira",
                    "descricao_kdp": "",
                    "keywords": [],
                    "categorias": [],
                    "idioma": "Português (Brasil)",
                    "preco_launch": "R$2,99",
                    "preco_normal": "R$9,90",
                    "kindle_unlimited": True,
                },
                ensure_ascii=False,
                indent=2,
            ),
        )
    if "cta" in enabled:
        _write_if_missing(
            workspace / files["cta_report"],
            json.dumps(
                {"tema": title, "promessa_central": "", "produtos": [], "proxima_acao": ""},
                ensure_ascii=False,
                indent=2,
            ),
        )
        _write_if_missing(
            workspace / files["cta_subagent"],
        json.dumps(
            {
                "tema": title,
                "promessa_central": "",
                "audiencia": "",
                "produtos_sugeridos": [],
                "ganchos_editoriais_por_capitulo": [],
                "ctas_recomendados": [],
                "riscos_de_incoerencia": [],
            },
            ensure_ascii=False,
            indent=2,
        ),
        )
        _write_if_missing(workspace / files["cta_subagent_brief"], build_cta_subagent_brief(title=title, workspace=workspace))
    _write_if_missing(workspace / files["stage_strategy"], build_stage_strategy(title=title))
    _write_if_missing(workspace / files["model_routing"], json.dumps(build_model_routing_payload(workspace), ensure_ascii=False, indent=2))


def render_package(workspace: Path, *, min_words: int = 15000) -> None:
    issues = validate_workspace(workspace, min_words=min_words)
    if issues:
        raise RuntimeError("Não foi possível renderizar o pacote:\n- " + "\n- ".join(issues))
    package = build_final_package(workspace)
    title = resolve_package_title(workspace, package.metadata)
    cta_path = package.files["cta_subagent"]
    cta_report_path = package.files["cta_report"]
    if cta_path.exists() and cta_report_path.exists():
        promote_cta_subagent_output(cta_path, cta_report_path, title=title)
    cta_payload = load_cta_payload(cta_report_path) if cta_report_path.exists() else {}
    ebook_markdown = package.files["ebook_markdown"].read_text(encoding="utf-8-sig")
    ebook_markdown = inject_cta_links(ebook_markdown, cta_payload)
    package.files["ebook_markdown"].write_text(ebook_markdown, encoding="utf-8")
    render_markdown_docx(ebook_markdown, package.files["ebook_docx"], fallback_title=title)
    _update_docx_toc(package.files["ebook_docx"])
    bonus_path = package.files["bonus_markdown"]
    if bonus_path.exists():
        bonus_markdown = bonus_path.read_text(encoding="utf-8-sig")
        render_markdown_docx(bonus_markdown, package.files["bonus_docx"], fallback_title=f"Bônus - {title}")
        _update_docx_toc(package.files["bonus_docx"])


def _update_docx_toc(path: Path) -> None:
    """Open the DOCX in Word via COM automation, update all TOC fields, and save. Silent no-op if Word is unavailable."""
    try:
        import win32com.client  # type: ignore[import]
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        try:
            doc = word.Documents.Open(str(path.resolve()))
            for toc in doc.TablesOfContents:
                toc.Update()
            doc.Fields.Update()
            doc.Save()
            doc.Close(False)
        finally:
            word.Quit()
    except Exception:
        pass  # Word not available — TOC field remains as placeholder


def prepare_cta_subagent_brief(workspace: Path) -> Path:
    package = build_final_package(workspace)
    title = package.metadata["title"]
    brief_path = package.files["cta_subagent_brief"]
    brief_path.write_text(build_cta_subagent_brief(title=title, workspace=workspace), encoding="utf-8")
    return brief_path


def prepare_stage_strategy(workspace: Path) -> Path:
    package = build_final_package(workspace)
    title = package.metadata["title"]
    strategy_path = package.files["stage_strategy"]
    strategy_path.write_text(build_stage_strategy(title=title), encoding="utf-8")
    return strategy_path


def prepare_model_routing(workspace: Path, *, profile: str | None = None) -> Path:
    package = build_final_package(workspace)
    routing_path = package.files["model_routing"]
    routing_path.write_text(
        json.dumps(build_model_routing_payload(workspace, profile=profile), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return routing_path


def prepare_codex_orchestration(workspace: Path, *, profile: str | None = None) -> Path:
    orchestration_path = workspace / "15_codex_orchestration.json"
    orchestration_path.write_text(
        json.dumps(build_codex_orchestration_payload(workspace, profile=profile), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return orchestration_path


def prepare_chapter_packet(workspace: Path, *, chapter_name: str) -> Path:
    package = build_final_package(workspace)
    packet_dir = workspace / "chapter-packets"
    packet_dir.mkdir(exist_ok=True)
    packet_path = packet_dir / f"{safe_slug(chapter_name)}.md"
    packet_path.write_text(build_chapter_packet(package, chapter_name=chapter_name), encoding="utf-8")
    return packet_path


def route_stage(workspace: Path, *, stage: str, chapter_name: str | None = None, profile: str | None = None) -> dict[str, Any]:
    package = build_final_package(workspace)
    active_profile = resolve_execution_profile(package.metadata, profile)
    routing_policy = load_model_routing_policy()
    stage_key = normalize_stage_name(stage)
    if stage_key not in routing_policy["stages"]:
        raise ValueError(f"Etapa nao suportada para roteamento automatico: {stage}")

    policy = routing_policy["stages"][stage_key]
    model = policy["model"]
    reasoning_effort = apply_profile_reasoning(policy["reasoning_effort"], active_profile)
    context_files = resolve_stage_context_files(package, stage_key, chapter_name=chapter_name)
    route = {
        "stage": stage_key,
        "model": model,
        "reasoning_effort": reasoning_effort,
        "context_files": [str(path) for path in context_files],
        "justification": policy["justification"],
        "execution_mode": policy.get("execution_mode", "single-agent"),
        "profile": active_profile,
        "checkpoint": build_checkpoint(stage_key, active_profile),
        "max_feedback_cycles": max_feedback_cycles_for_profile(active_profile),
    }
    if chapter_name:
        route["chapter"] = chapter_name
    return route


def run_editorial_stage(
    workspace: Path,
    *,
    stage: str,
    chapter_name: str | None = None,
    profile: str | None = None,
    feedback: str | None = None,
) -> Path:
    package = build_final_package(workspace)
    active_profile = resolve_execution_profile(package.metadata, profile)
    run_context = ensure_run_tracking(workspace, package.metadata, active_profile)
    try:
        route = route_stage(workspace, stage=stage, chapter_name=chapter_name, profile=profile)
        if feedback:
            record_run_event(
                run_context["events_path"],
                event_type="checkpoint_feedback",
                details={"stage": route["stage"], "chapter": chapter_name, "feedback": feedback.strip()},
            )
        record_run_event(
            run_context["events_path"],
            event_type="stage_started",
            details={"stage": route["stage"], "chapter": chapter_name, "profile": active_profile},
        )
        update_run_state(
            run_context["state_path"],
            status="running",
            stage=route["stage"],
            profile=active_profile,
        )
        stage_runs_dir = workspace / "stage-runs"
        stage_runs_dir.mkdir(exist_ok=True)
        suffix = f"-{safe_slug(chapter_name)}" if chapter_name else ""
        job_path = stage_runs_dir / f"{normalize_stage_name(stage)}{suffix}.json"
        payload = build_stage_job_payload(package, route, chapter_name=chapter_name)
        job_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        checkpoint_type = (payload.get("checkpoint") or {}).get("type")
        if checkpoint_type in {"approve", "select"}:
            record_run_event(
                run_context["events_path"],
                event_type="checkpoint_waiting",
                details={"stage": route["stage"], "chapter": chapter_name, "checkpoint": checkpoint_type},
            )
        record_run_event(
            run_context["events_path"],
            event_type="stage_completed",
            details={"stage": route["stage"], "chapter": chapter_name, "job_path": str(job_path)},
        )
        update_run_state(
            run_context["state_path"],
            status="running",
            stage=route["stage"],
            profile=active_profile,
        )
        return job_path
    except Exception as exc:
        record_run_event(
            run_context["events_path"],
            event_type="run_failed",
            details={"stage": stage, "chapter": chapter_name, "error": str(exc)},
        )
        update_run_state(
            run_context["state_path"],
            status="failed",
            stage=normalize_stage_name(stage),
            profile=active_profile,
            error=str(exc),
        )
        raise


def push_package(client: NotionClient, workspace: Path, *, draft_status: str) -> None:
    issues = validate_workspace(workspace, min_words=7000)
    if issues:
        raise RuntimeError("Não foi possível publicar o pacote:\n- " + "\n- ".join(issues))
    package = build_final_package(workspace)
    active_profile = resolve_execution_profile(package.metadata, None)
    run_context = ensure_run_tracking(workspace, package.metadata, active_profile)
    record_run_event(run_context["events_path"], event_type="stage_started", details={"stage": "push"})
    update_run_state(run_context["state_path"], status="running", stage="push", profile=active_profile)
    cta_path = package.files["cta_subagent"]
    cta_report_path = package.files["cta_report"]
    if cta_path.exists() and cta_report_path.exists():
        promote_cta_subagent_output(cta_path, cta_report_path, title=package.metadata["title"])
    page_id = package.metadata["page_id"]
    page = client.get_page(page_id)
    title = resolve_package_title(workspace, package.metadata)
    corrected_text = package.files["corrected_transcription"]
    ebook_docx = package.files["ebook_docx"]
    bonus_docx = package.files["bonus_docx"]
    if not ebook_docx.exists():
        raise RuntimeError("Renderize o DOCX do ebook antes do push.")
    runtime_agent = detect_runtime_agent()

    upload_tasks = [
        (page_id, "Corrigido", corrected_text),
        (page_id, "Ebook_HTML", ebook_docx),
    ]
    if bonus_docx.exists():
        upload_tasks.append((page_id, "Bonus_PDF", bonus_docx))
    with ThreadPoolExecutor(max_workers=len(upload_tasks)) as _pool:
        for _args in upload_tasks:
            _pool.submit(client.upload_file_property, *_args)

    ebook_markdown = package.files["ebook_markdown"].read_text(encoding="utf-8-sig")
    client.write_markdown_to_page(page_id, ebook_markdown)

    updates = build_push_updates(package, title=title, runtime_agent=runtime_agent, draft_status=draft_status)
    property_payload = client.build_property_payload(page, updates)
    if property_payload:
        client.update_page_properties(page_id, property_payload)
    client.set_page_workflow_status(page_id, "Pronto")
    record_run_event(run_context["events_path"], event_type="run_completed", details={"stage": "push", "status": draft_status})
    update_run_state(run_context["state_path"], status="completed", stage="push", profile=active_profile)


def _read_if_exists(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8-sig") if path.exists() else default


def build_push_updates(package: Any, *, title: str, runtime_agent: str, draft_status: str) -> dict[str, Any]:
    updates: dict[str, Any] = {
        "Nome_Ebook": title,
        "Data_Criacao": datetime.now().date().isoformat(),
        "Palavras_Ebook": count_words(package.files["ebook_markdown"].read_text(encoding="utf-8-sig")),
        "Resumo_Sermao": package.files["sermon_summary"].read_text(encoding="utf-8-sig"),
        "Blueprint_Ebook": package.files["ebook_blueprint"].read_text(encoding="utf-8-sig"),
        "Relatorio_Editorial": package.files["editorial_report"].read_text(encoding="utf-8-sig"),
        "Score_Qualidade": derive_quality_score(package.files["editorial_report"]),
        "Falhas_QA": collect_quality_failures(package.files["editorial_report"]),
        "IA Agente": runtime_agent,
        "Status": draft_status,
    }
    landing = _read_if_exists(package.files["landing_html"])
    if landing:
        updates["Landing_HTML"] = landing
    metadata = _read_if_exists(package.files["kdp_metadata"])
    if metadata:
        updates["Metadata_KDP"] = metadata
    cta_report_path = package.files["cta_report"]
    if cta_report_path.exists():
        updates["Relatorio_CTA"] = json.dumps(build_cta_delivery_report(cta_report_path), ensure_ascii=False, indent=2)
    return updates


def derive_quality_score(editorial_report_path: Path) -> int:
    text = editorial_report_path.read_text(encoding="utf-8-sig").lower()
    penalties = 0
    for token in ("pendência", "pendencias", "risco", "falha", "reprovação", "reprovacao"):
        penalties += text.count(token)
    return max(0, 100 - penalties * 5)


def collect_quality_failures(editorial_report_path: Path) -> str:
    text = editorial_report_path.read_text(encoding="utf-8-sig")
    failures = []
    for line in text.splitlines():
        if any(marker in line.lower() for marker in ("falha", "risco", "pendência", "pendencias", "reprovação", "reprovacao")):
            failures.append(line.strip())
    return "\n".join(failures[:20])


def detect_runtime_agent() -> str:
    env = {key.upper(): value for key, value in os.environ.items()}
    path_hints = " ".join(
        [
            str(Path.cwd()).casefold(),
            str(Path(__file__).resolve()).casefold(),
            env.get("CODEX_HOME", "").casefold(),
            env.get("HOME", "").casefold(),
            env.get("USERPROFILE", "").casefold(),
        ]
    )

    # Environment-first detection for sessions that expose explicit runtime tags.
    if any(key.startswith("CODEX_") for key in env):
        return "codex"
    if "ANTIGRAVITY" in env or "ANTIGRAV" in env or ".antigravity" in path_hints:
        return "antigravity"
    if any(key.startswith("CLAUDE") for key in env) or ".claude" in path_hints:
        return "claude"
    if any(key.startswith("CURSOR") for key in env) or ".cursor" in path_hints:
        return "cursor"
    if any(key.startswith("WINDSURF") for key in env) or ".windsurf" in path_hints:
        return "windsurf"

    # Fallback by installation path marker.
    if ".codex" in path_hints:
        return "codex"
    return "codex"


def build_cta_subagent_brief(*, title: str, workspace: Path) -> str:
    package = build_final_package(workspace)
    summary = read_excerpt(package.files["sermon_summary"], max_chars=3200)
    blueprint = read_excerpt(package.files["ebook_blueprint"], max_chars=3200)
    ebook_excerpt = read_excerpt(package.files["ebook_markdown"], max_chars=2200)
    return (
        f"# Briefing do Subagente CTA\n\n"
        f"## Tema do ebook\n\n{title}\n\n"
        f"## Objetivo\n\n"
        f"Gerar sugestoes comerciais discretas e coerentes com o sermao, sem desviar do eixo tematico do ebook. "
        f"O subagente nao pode escrever no ebook diretamente. Sua saida deve preencher apenas `11_cta_subagent.json`.\n\n"
        f"## Fontes obrigatorias\n\n"
        f"- `03_resumo_sermao.md`\n"
        f"- `04_blueprint_ebook.md`\n"
        f"- `06_ebook.md` apenas como apoio para ritmo e encaixe, nunca para mudar o argumento\n\n"
        f"## Criterios editoriais\n\n"
        f"- sugerir apenas produtos coerentes com a promessa central do sermao\n"
        f"- preferir 3 sugestoes discretas, no maximo 5\n"
        f"- usar linguagem pastoral, sobria e organica\n"
        f"- evitar publicidade agressiva, gatilhos artificiais ou ofertas genericas\n"
        f"- cada CTA precisa nascer de um ponto real do capitulo\n"
        f"- registrar riscos de incoerencia quando houver duvida\n\n"
        f"## Saida esperada em `11_cta_subagent.json`\n\n"
        f"- `tema`\n"
        f"- `promessa_central`\n"
        f"- `audiencia`\n"
        f"- `produtos_sugeridos`\n"
        f"- `ganchos_editoriais_por_capitulo`\n"
        f"- `ctas_recomendados`\n"
        f"- `riscos_de_incoerencia`\n\n"
        f"## Resumo do sermao\n\n{summary}\n\n"
        f"## Blueprint do ebook\n\n{blueprint}\n\n"
        f"## Trecho inicial do ebook\n\n{ebook_excerpt}\n"
    )


def read_excerpt(path: Path, *, max_chars: int) -> str:
    if not path.exists():
        return "(arquivo ainda nao disponivel)"
    text = path.read_text(encoding="utf-8-sig").strip()
    if not text:
        return "(arquivo vazio)"
    return text[:max_chars].rstrip()


def build_stage_strategy(*, title: str) -> str:
    return (
        f"# Estrategia de Tokens\n\n"
        f"## Projeto\n\n{title}\n\n"
        f"## Principio\n\n"
        f"Gastar mais contexto apenas nas decisoes editoriais nobres. Usar artefatos curtos e reutilizaveis no restante do fluxo.\n\n"
        f"## Etapas de alto investimento\n\n"
        f"- correcao cognitiva da transcricao\n"
        f"- blueprint do livro\n"
        f"- redacao dos capitulos\n"
        f"- critica editorial final\n\n"
        f"## Etapas de baixo investimento\n\n"
        f"- relatorio CTA\n"
        f"- metadata KDP\n"
        f"- landing page\n"
        f"- bonus\n"
        f"- consolidacao e renderizacao\n\n"
        f"## Regras de economia\n\n"
        f"- nunca reenviar a transcricao inteira se ja existir resumo e blueprint\n"
        f"- escrever e revisar por capitulo, nao o livro inteiro em toda rodada\n"
        f"- usar contexto minimo: promessa central, objetivo do capitulo, trecho relevante da fonte e checklist editorial curto\n"
        f"- usar subagentes apenas com briefing enxuto e saida estruturada\n"
        f"- criticar por problemas encontrados, nao recontando o manuscrito completo\n"
    )


def build_model_routing_payload(workspace: Path, *, profile: str | None = None) -> dict[str, Any]:
    package = build_final_package(workspace)
    title = package.metadata["title"]
    active_profile = resolve_execution_profile(package.metadata, profile)
    routing_policy = load_model_routing_policy()
    stages: dict[str, Any] = {}
    for stage_name in routing_policy["stage_order"]:
        chapter_name = "Capítulo 1" if stage_name in {"chapter_writing", "chapter_revision"} else None
        try:
            route = route_stage(workspace, stage=stage_name, chapter_name=chapter_name, profile=active_profile)
        except Exception:
            route = {
                "stage": stage_name,
                "model": routing_policy["stages"][stage_name]["model"],
                "reasoning_effort": apply_profile_reasoning(
                    routing_policy["stages"][stage_name]["reasoning_effort"],
                    active_profile,
                ),
                "context_files": [],
                "justification": routing_policy["stages"][stage_name]["justification"],
                "execution_mode": routing_policy["stages"][stage_name].get("execution_mode", "single-agent"),
                "profile": active_profile,
                "checkpoint": build_checkpoint(stage_name, active_profile),
                "max_feedback_cycles": max_feedback_cycles_for_profile(active_profile),
            }
        stages[stage_name] = route
    return {
        "ebook_title": title,
        "generated_at": datetime.now().isoformat(),
        "execution_profile": active_profile,
        "routing_policy_version": routing_policy["version"],
        "stages": stages,
    }


def build_codex_orchestration_payload(workspace: Path, *, profile: str | None = None) -> dict[str, Any]:
    package = build_final_package(workspace)
    active_profile = resolve_execution_profile(package.metadata, profile)
    routing_policy = load_model_routing_policy()
    chapters = list_orchestration_chapters(package)
    steps: list[dict[str, Any]] = []
    enabled_artifacts = get_enabled_artifacts(workspace)
    enabled_stages = {_ARTIFACT_STAGE_MAP[k] for k in enabled_artifacts}

    PARALLEL_GROUPS = {
        "chapter_writing": "chapters",
        "chapter_revision": "chapter_revision",
        "metadata_kdp": "auxiliary_artifacts",
        "landing_page": "auxiliary_artifacts",
        "bonus_asset": "auxiliary_artifacts",
    }
    # Artifact stages that can be disabled via --artifacts flag
    ARTIFACT_STAGES = frozenset(_ARTIFACT_STAGE_MAP.values())

    PARALLEL_GROUPS = {
        "chapter_writing": "chapters",
        "chapter_revision": "chapter_revision",
        "metadata_kdp": "auxiliary_artifacts",
        "landing_page": "auxiliary_artifacts",
        "bonus_asset": "auxiliary_artifacts",
    }

    for stage_name in routing_policy["stage_order"]:
        if stage_name in ARTIFACT_STAGES and stage_name not in enabled_stages:
            continue
        chapter_targets = chapters if stage_name in {"chapter_writing", "chapter_revision"} else [None]
        for chapter_name in chapter_targets:
            route = route_stage(workspace, stage=stage_name, chapter_name=chapter_name, profile=active_profile)
            suffix = f"-{safe_slug(chapter_name)}" if chapter_name else ""
            job_path = workspace / "stage-runs" / f"{stage_name}{suffix}.json"
            payload = build_stage_job_payload(package, route, chapter_name=chapter_name)
            steps.append(
                {
                    "stage": stage_name,
                    "chapter": chapter_name,
                    "job_path": str(job_path),
                    "spawn_subagent": True,
                    "subagent_role": "worker",
                    "model": route["model"],
                    "reasoning_effort": route["reasoning_effort"],
                    "checkpoint": route["checkpoint"],
                    "max_feedback_cycles": route["max_feedback_cycles"],
                    "context_files": route["context_files"],
                    "output_target": payload["output_target"],
                    "instructions": payload["instructions"],
                    "success_criteria": payload["success_criteria"],
                    "ownership": infer_stage_ownership(stage_name, chapter_name=chapter_name),
                    "parallel_group": PARALLEL_GROUPS.get(stage_name),
                }
            )

    return {
        "ebook_title": package.metadata["title"],
        "generated_at": datetime.now().isoformat(),
        "execution_profile": active_profile,
        "orchestration_mode": "codex-subagents-parallel-chapters",
        "main_agent_role": "orchestrator",
        "subagent_contract": {
            "required": True,
            "policy_source": "references/model-routing-policy.json",
            "rule": (
                "Toda etapa editorial deve ser executada via subagente com o modelo fixo da policy. "
                "Etapas com o mesmo parallel_group devem ser lançadas simultaneamente como subagentes paralelos. "
                "O agente principal orquestra, delega em paralelo onde indicado, integra e valida."
            ),
        },
        "steps": steps,
        "execution_hint": (
            "Execute all steps with the same parallel_group simultaneously as parallel subagents. "
            "Steps without parallel_group run sequentially in stage_order. "
            "auxiliary_artifacts can start as soon as book_blueprint is approved, in parallel with chapter_writing."
        ),
    }


def load_model_routing_policy() -> dict[str, Any]:
    path = Path(__file__).resolve().parents[1] / "references" / "model-routing-policy.json"
    return json.loads(path.read_text(encoding="utf-8-sig"))


def normalize_stage_name(stage: str) -> str:
    return stage.strip().lower().replace("-", "_").replace(" ", "_")


def resolve_stage_context_files(package: Any, stage_name: str, *, chapter_name: str | None) -> list[Path]:
    files = package.files
    if stage_name == "transcription_correction":
        return [
            files["raw_transcription"],
            Path(__file__).resolve().parents[1] / "references" / "transcription-editorial-guidelines.md",
        ]
    if stage_name == "sermon_summary":
        return [files["corrected_transcription"], files["stage_strategy"]]
    if stage_name == "book_blueprint":
        return [
            files["sermon_summary"],
            Path(__file__).resolve().parents[1] / "references" / "sermon-to-book-playbook.md",
            files["stage_strategy"],
        ]
    if stage_name in {"chapter_writing", "chapter_revision"}:
        chapter = chapter_name or "Capítulo 1"
        packet_path = package.workspace / "chapter-packets" / f"{safe_slug(chapter)}.md"
        if not packet_path.exists():
            packet_path = prepare_chapter_packet(package.workspace, chapter_name=chapter)
        return [
            packet_path,
            files["sermon_summary"],
            files["ebook_blueprint"],
            files["stage_strategy"],
            Path(__file__).resolve().parents[1] / "references" / "author-voice-profile.md",
        ]
    if stage_name == "framing_sections":
        return [
            files["ebook_markdown"],
            files["ebook_blueprint"],
            files["sermon_summary"],
            files["stage_strategy"],
            Path(__file__).resolve().parents[1] / "references" / "author-voice-profile.md",
        ]
    if stage_name == "final_critique":
        return [files["ebook_markdown"], files["sermon_summary"], files["editorial_report"], files["stage_strategy"]]
    if stage_name == "cta_subagent":
        brief_path = files["cta_subagent_brief"]
        if not brief_path.exists():
            brief_path = prepare_cta_subagent_brief(package.workspace)
        return [brief_path, files["cta_subagent"]]
    if stage_name in {"metadata_kdp", "landing_page", "bonus_asset"}:
        return [files["sermon_summary"], files["ebook_blueprint"], files["stage_strategy"]]
    return [files["stage_strategy"]]


def build_stage_job_payload(package: Any, route: dict[str, Any], *, chapter_name: str | None) -> dict[str, Any]:
    stage = route["stage"]
    output_target = infer_stage_output_target(package, stage)
    previous_attempts = count_stage_feedback_attempts(package.workspace, stage, chapter_name=chapter_name)
    return {
        "generated_at": datetime.now().isoformat(),
        "stage": stage,
        "chapter": chapter_name,
        "profile": route.get("profile", DEFAULT_EXECUTION_PROFILE),
        "execution_mode": route["execution_mode"],
        "checkpoint": route.get("checkpoint", {"type": "approve"}),
        "max_feedback_cycles": route.get("max_feedback_cycles", 2),
        "previous_attempts": previous_attempts,
        "model": route["model"],
        "reasoning_effort": route["reasoning_effort"],
        "justification": route["justification"],
        "context_files": route["context_files"],
        "output_target": str(output_target) if output_target else "",
        "instructions": build_stage_instructions(stage, package, chapter_name=chapter_name),
        "success_criteria": build_stage_success_criteria(stage),
        "codex_subagent": {
            "required": route["execution_mode"] == "subagent",
            "agent_type": "worker",
            "model": route["model"],
            "reasoning_effort": route["reasoning_effort"],
            "ownership": infer_stage_ownership(stage, chapter_name=chapter_name),
            "handoff_rule": "O agente principal nao executa a etapa editorial localmente; deve delegar para subagente e consolidar o resultado.",
        },
    }


def count_stage_feedback_attempts(workspace: Path, stage: str, *, chapter_name: str | None) -> int:
    manifest_path = workspace / "manifest.json"
    if not manifest_path.exists():
        return 0
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        run_id = manifest.get("run_id")
        if not run_id:
            return 0
        events_path = workspace / "runs" / str(run_id) / "events.jsonl"
        if not events_path.exists():
            return 0
        total = 0
        for line in events_path.read_text(encoding="utf-8-sig").splitlines():
            if not line.strip():
                continue
            event = json.loads(line)
            if event.get("event_type") != "checkpoint_feedback":
                continue
            details = event.get("details") or {}
            if details.get("stage") != stage:
                continue
            if chapter_name and details.get("chapter") != chapter_name:
                continue
            total += 1
        return total
    except Exception:
        return 0


def infer_stage_output_target(package: Any, stage: str) -> Path | None:
    files = package.files
    mapping = {
        "transcription_correction": files["corrected_transcription"],
        "sermon_summary": files["sermon_summary"],
        "book_blueprint": files["ebook_blueprint"],
        "chapter_writing": files["ebook_markdown"],
        "chapter_revision": files["ebook_markdown"],
        "framing_sections": files["ebook_markdown"],
        "final_critique": files["editorial_report"],
        "cta_subagent": files["cta_subagent"],
        "metadata_kdp": files["kdp_metadata"],
        "landing_page": files["landing_html"],
        "bonus_asset": files["bonus_markdown"],
    }
    return mapping.get(stage)


def build_stage_instructions(stage: str, package: Any, *, chapter_name: str | None) -> str:
    title = package.metadata["title"]
    source_property = package.metadata.get("source_property") or DEFAULT_CORRECTED_PROPERTY
    if stage == "transcription_correction":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n"
            f"Corrija a transcricao em PT-BR com maxima fidelidade ao sermao de '{title}'.\n"
            f"Melhore ortografia, pontuacao, acentuacao e sintaxe. Remova ruido de ASR, "
            f"juncoes artificiais de frases e duplicacoes mecanicas.\n"
            f"NAO invente conteudo, nao reinterprete a teologia do pregador, nao transforme a transcricao em ebook.\n"
            f"Preserve a voz oral e o calor pastoral do pregador onde fazem parte da mensagem.\n"
            f"Quando o audio for ambiguo, use a formulacao mais conservadora e segura.\n"
            f"Normalize referencias biblicas quando clara a intencao (ex: 'romanos oito vinte e oito' -> 'Romanos 8.28').\n"
            f"Grave o resultado em 02_corrigido.txt."
        )
    if stage == "sermon_summary":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n"
            f"Leia a transcricao corrigida e produza um resumo fiel do sermao de '{title}'. "
            f"O resumo deve conter obrigatoriamente:\n"
            f"1. TESE CENTRAL: a afirmacao principal do pregador em uma frase.\n"
            f"2. TEXTO BIBLICO PRINCIPAL: referencia e texto do versiculo central. Traducao NVI.\n"
            f"3. TEXTOS BIBLICOS SECUNDARIOS: demais referencias usadas, com versiculo e traducao NVI.\n"
            f"4. MOVIMENTOS DO ARGUMENTO: os passos logicos ou narrativos do sermao, na ordem em que aparecem.\n"
            f"5. ILUSTRACOES E HISTORIAS: liste cada ilustracao, historia ou exemplo concreto que o pregador usou, "
            f"com trecho aproximado do sermao que a ancora.\n"
            f"6. APLICACOES PASTORAIS: o que o pregador pediu ou convidou o ouvinte a fazer - especifico, nao generico.\n"
            f"7. FORA DO ESCOPO - EXPLICITO: liste temas que o pregador NAO abordou ou que estao alem do que o sermao sustenta, incluindo topicos teologicos adjacentes nao desenvolvidos. Esta secao e critica para evitar que o ebook divague.\n"
            f"Grave em 03_resumo_sermao.md."
        )
    if stage == "book_blueprint":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n{BIBLICAL_TEXT_GUARDRAIL}\n\n{PERSUASIVE_EBOOK_GUARDRAIL}\n\n{FIXED_PERSUASIVE_CHAPTER_ARCHITECTURE}\n\n"
            f"Transforme o resumo do sermao de '{title}' em um blueprint editorial de ebook.\n\n"
            f"ANCORA: cada capitulo deve ser derivavel do sermao - seja de conteudo explicitamente presente ou implicitamente contido no argumento do pregador. Expansao legitima significa aprofundar o que o pregador disse, nao adicionar temas, aplicacoes ou doutrinas que ele nao abordou.\n\n"
            f"PADRAO ESTRUTURAL PREFERENCIAL:\n"
            f"Salvo limitacao real do sermao, use a espinha dorsal da generate-persuasive-ebooks: subtitulo na linha 'Um guia biblico e pratico para...', introducao confessional, 8 capitulos, um capitulo de diagnostico do erro/crenca, um capitulo 'O que a Biblia realmente diz', um capitulo com framework pratico numerado, capitulo 7 com aplicacao para membros/lideres/pastores e fechamento pastoral.\n\n"
            f"TITULO DO LIVRO:\n"
            f"O titulo nao e descricao - e promessa em forma de tensao, convite ou afirmacao contra-intuitiva. Bons titulos pastorais capturam: a dor ou busca do leitor + a saida que o livro oferece. Proponha 3 opcoes de titulo com justificativa breve e indique a recomendada.\n\n"
            f"TITULOS DE CAPITULOS:\n"
            f"Cada titulo deve ser marcante, nao apenas descritivo. Deve capturar o argumento exclusivo do capitulo de forma que provoque ou prometa algo especifico.\n\n"
            f"ESTRUTURA:\n"
            f"Defina: promessa central em uma frase, leitor ideal especifico e sumario detalhado.\n"
            f"Cada capitulo deve ter angulo distinto e intransferivel - nenhum pode sobrepor o tema de outro.\n"
            f"Use obrigatoriamente o template de 04_blueprint_ebook.md. Para cada capitulo especifique com clareza: "
            f"(a) objetivo neuroemocional, (b) papel fixo no arco, (c) crenca ou leitura defeituosa a quebrar, "
            f"(d) dor latente a amplificar, (e) nova identidade, lente ou modelo mental a propor, (f) ancora biblica, "
            f"(g) trecho do sermao que ancora, (h) ganho do leitor ao final, (i) transicao para o proximo capitulo.\n"
            f"No Capitulo 2, inclua analogia principal. No Capitulo 6, liste os passos numerados. No Capitulo 7, separe aplicacoes para membros, lideres e pastores. No Capitulo 8, explicite o custo de continuar igual e a chamada implicita.\n\n"
            f"Se o blueprint fugir desse padrao, explique objetivamente por que o proprio sermao exige o desvio.\n\n"
            f"Grave em 04_blueprint_ebook.md."
        )
    if stage == "chapter_writing":
        chapter_label = chapter_name or "Capitulo"
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n{BIBLICAL_TEXT_GUARDRAIL}\n\n{PERSUASIVE_EBOOK_GUARDRAIL}\n\n{FIXED_PERSUASIVE_CHAPTER_ARCHITECTURE}\n\n"
            f"Escreva ou expanda apenas {chapter_label} do ebook '{title}'. Use o chapter packet e o blueprint como contexto principal. Leia o perfil de voz autoral em references/author-voice-profile.md antes de comecar.\n\n"
            f"PAPEL FIXO DESTE CAPITULO:\n"
            f"{chapter_role_spec(chapter_label)}\n\n"
            f"VOZ E REGISTRO:\n"
            f"Escreva como Pr. Filipe Ivo Pereira - culto e acessivel, pastoral e literario, profundo sem ser verboso. Nao e autoajuda com verniz espiritual. E fe robusta que encontra a vida real do leitor.\n\n"
            f"PADRAO generate-persuasive-ebooks:\n"
            f"Cada capitulo deve reproduzir a cadencia dos modelos aprovados: reconhecer a experiencia real do leitor, aprofundar a dor ou o custo silencioso, desmontar uma crenca errada, introduzir nova perspectiva biblica e psicologica, e conduzir a uma pratica esperancosa. O texto deve soar como livro persuasivo-pastoral de alta qualidade, nao como capitulo generico cristao.\n\n"
            f"FIDELIDADE AO SERMAO (REGRA DE OURO):\n"
            f"Desenvolva apenas argumentos, ilustracoes e pontos presentes na transcricao. Expansao legitima = aprofundar o que esta implicitamente presente no argumento do pregador. Nao adicione temas novos, doutrinas nao abordadas ou analogias externas ao sermao.\n\n"
            f"CITACOES BIBLICAS:\n"
            f"Traducao padrao: NVI (Nova Versao Internacional). Use consistentemente. Cite sempre a referencia completa (ex: Joao 3.16). Sempre que o contexto estiver pedindo embasamento biblico explicito, traga o versiculo completo, nao apenas a ideia resumida. No markdown, envolva todo texto biblico citado integralmente em *italico* para o DOCX final renderizar em italico e Times New Roman. Integre o versiculo no argumento - depois de citar, desenvolva o que ele revela. Nao use versiculos como ornamento decorativo.\n\n"
            f"REQUISITOS ESTRUTURAIS:\n"
            f"(1) Minimo de 900 palavras de conteudo real.\n"
            f"(2) ABERTURA PASTORAL: abra com cena narrativa, tensao existencial real ou pergunta que o leitor ja carrega. Nao abra com estatistica generica, definicao de dicionario ou frase motivacional. A abertura boa toca onde o leitor doi ou onde ele tem duvida genuina.\n"
            f"(3) Desenvolva o argumento em pelo menos 3 movimentos distintos com profundidade teologica e pastoral, mantendo dialogo perceptivel e organico com o texto biblico de origem.\n"
            f"(4) RITMO: varie o tamanho de frases e paragrafos. Intercale paragrafos longos com frases curtas de impacto. Maximo 2 perguntas retoricas por secao. Evite paragrafos que comecam com 'E importante', 'Devemos', 'Precisamos' - reescreva com verbo ou imagem.\n"
            f"(5) ZERO cliches genericos evangelicos que poderiam estar em qualquer livro cristao.\n"
            f"(6) Nao repita historias, ilustracoes ou exemplos ja usados em outros capitulos.\n"
            f"(7) Reproduza o padrao dos modelos: diagnostico preciso, graca antes de cobranca, aplicacao concreta sem checklist seco, integracao organica entre Biblia e psicologia, e progressao emocional planejada.\n"
            f"(8) Ative simultaneamente reptiliano, limbico e neocortex: risco e consequencia, conflito e pertencimento, causa e efeito, explicacao e direcao pratica.\n"
            f"(9) ENCADEAMENTO: a ultima ideia do capitulo deve resolver o que prometeu e abrir expectativa para o proximo.\n\n"
            f"FRASE DE EFEITO (OBRIGATORIA):\n"
            f"Ao final do conteudo do capitulo, escreva a frase de efeito no formato exato:\n"
            f"<!-- EFEITO: sua frase aqui -->\n"
            f"A frase deve: ter 80 a 200 caracteres; capturar a tensao central do capitulo em forma aforistica; conter conflito humano reconhecivel + verdade biblica ou pastoral + convite implicito a transformacao. Deve ser especifica para este capitulo - nao poderia estar em outro livro cristao.\n\n"
            f"Titulo no padrao 'Capitulo N: Nome do Capitulo'. Nao inclua bonus, guias, devocionais, desafios ou apendice no ebook. Atualize 06_ebook.md sem reescrever capitulos fora do escopo."
        )
    if stage == "chapter_revision":
        chapter_label = chapter_name or "Capitulo"
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n{BIBLICAL_TEXT_GUARDRAIL}\n\n{PERSUASIVE_EBOOK_GUARDRAIL}\n\n{FIXED_PERSUASIVE_CHAPTER_ARCHITECTURE}\n\n"
            f"Revise apenas {chapter_label} do ebook '{title}'. Consulte o perfil de voz autoral em references/author-voice-profile.md.\n\n"
            f"PAPEL FIXO DESTE CAPITULO:\n"
            f"{chapter_role_spec(chapter_label)}\n\n"
            f"(1) FIDELIDADE PASTORAL: o conteudo deve ser rastreavel ao sermao - explicitamente citado ou implicitamente presente no argumento do pregador. Remova apenas o que e invencao externa, nao o desenvolvimento legitimo do que o pregador disse.\n"
            f"(2) VOZ: elimine frases genericas que poderiam estar em qualquer livro cristao. Fortifique a voz pastoral especifica - culta, acessivel, com peso espiritual real.\n"
            f"(3) CITACOES BIBLICAS: todos os versiculos usam NVI? Tem referencia completa? Quando o argumento exige embasamento explicito, o versiculo aparece por extenso? No markdown, o texto biblico integral esta em *italico* para renderizar em Times New Roman no DOCX? Sao desenvolvidos apos a citacao (nao apenas decorativos)?\n"
            f"(4) ABERTURA: se nao ancorar o leitor com tensao real nos primeiros paragrafos, reescreva. Abertura forte toca onde o leitor doi ou onde ele tem duvida genuina.\n"
            f"(5) RITMO: verifique variacao de tamanho de frases e paragrafos. Paragrafos que comecam com 'E importante', 'Devemos', 'Precisamos' - reescreva.\n"
            f"(6) ARGUMENTO: confirme pelo menos 3 movimentos distintos. Cada um deve avancar, nao repetir o anterior.\n"
            f"(7) PROFUNDIDADE TEOLOGICA: as afirmacoes espirituais tem fundamento biblico? O leitor sai convicto ou apenas emocionado? As aplicacoes sao especificas e praticas?\n"
            f"(8) PADRAO generate-persuasive-ebooks: confirme se o capitulo cumpre o papel fixo do numero do capitulo, tem reconhecimento imediato, progressao de dor/diagnostico/revelacao/pratica, e reposicionamento de identidade. Se soar generico ou fora da cadencia dos modelos, reescreva.\n"
            f"(9) CONEXAO BIBLICA: se qualquer trecho soar apenas como reflexao autonoma do autor, reforce a interacao explicita e organica com a passagem biblica de origem.\n"
            f"(10) Verifique se a engenharia emocional esta ativa: risco, perda, conflito interno, alivio plausivel, explicacao clara e progressao causa -> efeito -> solucao.\n"
            f"(11) FRASE DE EFEITO: verifique que existe o marcador <!-- EFEITO: ... --> ao final do capitulo. Se ausente ou fraco, escreva: 80-200 chars, aforistica, com tensao + verdade + transformacao, especifica.\n"
            f"(12) ENCADEAMENTO: o fechamento prepara o leitor para o proximo capitulo ou cristaliza a transformacao?\n\n"
            f"Minimo 800 palavras apos a revisao. Titulo no padrao 'Capitulo N: Nome do Capitulo'. Remova qualquer bonus, guia, devocional, desafio ou apendice que tenha entrado no ebook. Atualize 06_ebook.md sem alterar o restante do livro."
        )
    if stage == "framing_sections":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n{PERSUASIVE_EBOOK_GUARDRAIL}\n\n"
            f"Escreva Prefacio, Introducao e Conclusao do ebook '{title}' somente depois de ler todo o conteudo ja escrito. Consulte o perfil de voz autoral em references/author-voice-profile.md.\n\n"
            f"PREFACIO (min. 600 palavras):\n"
            f"Tom confessional, caloroso e honesto - o autor fala diretamente ao leitor como pastor, nao como escritor distante. Deve conter: (a) por que este sermao se tornou livro - o que motivou o pastor a preserva-lo; (b) quem e o leitor ideal e como o pastor o conhece - nomeie a dor ou a busca especifica dessa pessoa; (c) o que o leitor pode esperar - nao lista de capitulos, mas promessa de experiencia.\n\n"
            f"INTRODUCAO (min. 600 palavras):\n"
            f"Abra com cena narrativa, historia ou tensao que ancora o leitor na realidade que o livro vai tratar. Nao comece com definicoes ou perguntas retoricas soltas. Deve conter: (a) o problema central que o leitor carrega - nomeado com precisao e compaixao; (b) por que as respostas comuns falham ou sao insuficientes; (c) a promessa concreta do livro em uma frase forte; (d) apresentacao do arco dos capitulos de forma que motive - nao indice narrado, mas trailer da jornada.\n\n"
            f"CONCLUSAO (min. 600 palavras):\n"
            f"Nao e resumo - e ponto de chegada. Sintetize a transformacao que o leitor atravessou, nao repita os capitulos. Reforce a tese central com a forca de quem acabou de sustenta-la no livro inteiro. Convide a aplicacao concreta e imediata - especifica ao tema do livro, nao generica. Termine com autoridade pastoral e esperanca cristocentrica. A ultima frase do livro deve ser memoravel. Cada secao deve ter mais de 500 palavras - os minimos acima sao de qualidade, nao teto.\n\n"
            f"Alinhe as tres secoes ao padrao dos modelos: vulnerabilidade antes de autoridade, promessa pastoral clara, linguagem acessivel, e fechamento com esperanca praticavel.\n\n"
            f"Atualize 06_ebook.md sem alterar capitulos principais."
        )
    if stage == "final_critique":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n{BIBLICAL_TEXT_GUARDRAIL}\n\n{PERSUASIVE_EBOOK_GUARDRAIL}\n\n{FIXED_PERSUASIVE_CHAPTER_ARCHITECTURE}\n\n"
            f"Faca a critica editorial final do ebook '{title}'. Registre tudo em 05_relatorio_editorial.md:\n\n"
            f"1. CONTAGEM: total de palavras e por secao (Prefacio, Introducao, cada capitulo, Conclusao).\n"
            f"2. FIDELIDADE TEMATICA: o ebook honra a tese central e as ilustracoes do sermao? Aponte desvios com citacao do trecho e indicacao do que esta fora do sermao.\n"
            f"3. PROFUNDIDADE TEOLOGICA: as afirmacoes espirituais tem fundamento biblico solido? O leitor sai convicto ou apenas emocionado? Ha superficialidade que reduz fe a motivacao? As aplicacoes pastorais sao especificas e praticas ou genericas ('ore mais', 'leia a Biblia')?\n"
            f"4. REPETICOES: liste frases, historias ou argumentos repetidos entre secoes com citacao exata.\n"
            f"5. QUALIDADE LITERARIA: aponte aberturas fracas, fechamentos sem forca, paragrafos genericos que poderiam estar em qualquer livro cristao, cliches evangelicos, ritmo monotono.\n"
            f"6. CONFORMIDADE COM generate-persuasive-ebooks: o livro reproduz materialmente a forma de escrever, a arquitetura, o tom, a voz, o ritmo e a logica dos modelos aprovados? Aponte quebras de padrao.\n"
            f"7. CITACOES BIBLICAS: todas usam NVI? Todas tem referencia completa (livro.cap.vers)? Quando o argumento exige embasamento explicito, os versiculos aparecem por extenso? No markdown, o texto biblico integral esta em *italico* para renderizar em Times New Roman no DOCX? Os versiculos sao desenvolvidos apos a citacao ou apenas decorativos?\n"
            f"8. FRASES DE EFEITO: cada capitulo principal tem marcador <!-- EFEITO: ... -->? As frases sao especificas e aforisticas ou genericas?\n"
            f"9. ESTRUTURA FIXA POR CAPITULO: confirme ou reprove se Capitulo 1 abre loop mental, Capitulo 2 gera AHA pela causa raiz, Capitulo 3 reposiciona identidade e acao, Capitulo 5 explicita o que a Biblia realmente diz, Capitulo 6 oferece framework numerado, Capitulo 7 separa membros/lideres/pastores e Capitulo 8 fecha com custo de continuar igual + convite implicito.\n"
            f"10. ENGENHARIA NEUROEMOCIONAL: confirme se o livro ativa simultaneamente reptiliano, limbico e neocortex sem parecer manipulativo. Aponte capitulos que perderam risco, conflito, pertencimento, clareza causal ou direcao pratica.\n"
            f"11. PROGRESSAO E MOMENTUM: o leitor vai querer continuar de um capitulo ao proximo? O encadeamento entre capitulos e explicito? O arco promessa-desenvolvimento-resolucao esta claro?\n"
            f"12. CONEXAO BIBLICA: verifique se cada capitulo permanece em interacao real com o texto biblico de origem, e aponte trechos que estejam soando apenas como opiniao do autor sem ancoragem biblica suficiente.\n"
            f"13. VOZ AUTORAL: o texto soa como Pr. Filipe - culto, pastoral, acessivel, com peso espiritual real? Ou soa como escrita generica?\n"
            f"14. GATES DE PUBLICACAO - confirme ou reprove cada item:\n"
            f"    - total >= 15.000 palavras\n"
            f"    - Prefacio/Introducao/Conclusao >= 500 palavras cada\n"
            f"    - cada capitulo >= 800 palavras\n"
            f"    - todos os capitulos principais tem frase de efeito\n"
            f"    - zero desvios tematicos graves\n"
            f"    - aplicacoes pastorais sao praticas e especificas\n"
            f"    - a arquitetura fixa por capitulo foi respeitada ou o desvio foi justificado pelo sermao\n"
            f"    - o livro gera identificacao, revela causa invisivel, reposiciona identidade e conduz a uma decisao implicita\n"
            f"    - conformidade material com o padrao da generate-persuasive-ebooks e com os modelos aprovados\n"
            f"    - citacoes biblicas com referencia completa e na NVI, com versiculo por extenso quando o argumento exigir embasamento explicito\n"
            f"    - conexao biblica continua com a passagem de origem\n"
            f"Use a palavra 'reprovacao' se algum gate falhar."
        )
    if stage == "cta_subagent":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n"
            f"Atue como subagente de curadoria CTA do ebook '{title}'. Leia apenas o briefing curto e proponha ofertas discretas, coerentes e naturais. Grave somente em 11_cta_subagent.json."
        )
    if stage == "metadata_kdp":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n"
            f"Gere os metadados KDP completos para '{title}' em 09_metadata_kdp.json.\n\n"
            f"CAMPOS OBRIGATORIOS:\n"
            f"- title: titulo exato do ebook\n"
            f"- subtitle: subtitulo que completa a promessa (max. 150 chars)\n"
            f"- author: 'Filipe Ivo Pereira'\n"
            f"- description: 600 a 1000 caracteres. Estrutura: (1) frase de abertura que nomeia a dor ou busca do leitor; (2) o que este livro oferece e como; (3) para quem e; (4) chamada a acao. Use linguagem natural de mercado BR, nao jargao de marketing.\n"
            f"- keywords: exatamente 7 palavras-chave otimizadas para busca na Amazon Brasil. Pense no que o leitor BR procura, nao no que descreve o livro academicamente.\n"
            f"- categories: 2 categorias do catalogo Amazon KDP Brasil (ex: 'Religiao e Espiritualidade > Cristao > Vida Crista').\n"
            f"- language: 'pt'\n"
            f"- price_brl: sugestao de preco Kindle em BRL (entre R$ 9,99 e R$ 29,99).\n"
            f"- kindle_unlimited: true\n"
            f"- series: null\n\n"
            f"Grave em 09_metadata_kdp.json."
        )
    if stage == "landing_page":
        return f"{PTBR_UNICODE_GUARDRAIL}\n\nGere uma landing page simples e coerente com a promessa de '{title}' em 07_landing.html."
    if stage == "bonus_asset":
        return (
            f"{PTBR_UNICODE_GUARDRAIL}\n\n"
            f"Gere o bonus do ebook '{title}' em 08_bonus.md.\n\n"
            f"TIPO: escolha o formato mais adequado ao tema do livro:\n"
            f"(a) GUIA DE ESTUDO - 5 a 7 sessoes com perguntas reflexivas reais para grupos ou leitura pessoal;\n"
            f"(b) DEVOCIONAL DE 7 DIAS - reflexoes diarias de 300-400 palavras com texto biblico (NVI), meditacao e oracao sugerida;\n"
            f"(c) ROTEIRO DE APLICACAO - plano de 4 semanas para aplicar o ensinamento central em areas especificas da vida.\n\n"
            f"REQUISITOS:\n"
            f"- Minimo 2.000 palavras de conteudo real\n"
            f"- Derivado do mesmo eixo tematico do livro - nao repete capitulos, mas aprofunda ou aplica\n"
            f"- Mesmo registro de voz do livro (consulte references/author-voice-profile.md)\n"
            f"- Citacoes biblicas em NVI com referencia completa\n"
            f"- Valor editorial real - nao e apendice de relaxamento\n"
            f"- Nao pode ir para 06_ebook.md\n\n"
            f"Grave em 08_bonus.md."
        )
    return f"{PTBR_UNICODE_GUARDRAIL}\n\nExecute a etapa {stage} com fidelidade ao material do workspace."


def build_stage_success_criteria(stage: str) -> list[str]:
    common = [
        "fidelidade ao sermao",
        "aderencia ao escopo",
        "texto natural em PT-BR",
        "voz pastoral do autor",
        "conexao continua com o texto biblico de origem",
    ]
    stage_specific = {
        "transcription_correction": ["sem ruido mecanico", "sem invencao de conteudo", "referencias biblicas normalizadas"],
        "sermon_summary": ["tese central clara", "versiculos completos com referencia NVI", "limites de extrapolacao explicitos", "aplicacoes pastorais especificas"],
        "book_blueprint": ["3 opcoes de titulo com justificativa", "titulos de capitulo marcantes", "capitulos com angulo distinto", "encadeamento entre capitulos definido", "ancora biblica explicita por capitulo", "aderencia ao padrao generate-persuasive-ebooks", "arco hook-tensao-revelacao-transformacao", "8 capitulos no padrao fixo ou desvio justificado", "objetivo neuroemocional por capitulo", "crenca quebrada, dor latente, nova identidade e transicao descritas por capitulo"],
        "chapter_writing": ["minimo 900 palavras", "abertura pastoral que ancora o leitor", "3 movimentos de argumento distintos", "zero cliches genericos evangelicos", "citacoes biblicas em NVI com referencia", "versiculo completo quando o argumento exigir embasamento explicito", "texto biblico integral em markdown italico para DOCX Times New Roman", "frase de efeito <!-- EFEITO: --> ao final", "encadeamento com proximo capitulo", "interacao organica com a passagem biblica", "cadencia generate-persuasive-ebooks", "integracao biblia-psicologia-pratica", "papel fixo do numero do capitulo respeitado", "engenharia reptiliano-limbico-neocortex ativa"],
        "chapter_revision": ["minimo 800 palavras", "fidelidade ao sermao preservada (explicito ou implicito)", "citacoes biblicas NVI com referencia e desenvolvidas", "versiculo completo quando o argumento exigir embasamento explicito", "texto biblico integral em markdown italico para DOCX Times New Roman", "abertura e fechamento fortes", "sem repeticoes internas", "frase de efeito presente e especifica", "ancoragem biblica reforcada", "conformidade com generate-persuasive-ebooks", "papel fixo do capitulo auditado", "identificacao, AHA ou reposicionamento presentes conforme o numero do capitulo"],
        "framing_sections": ["prefacio >= 500 palavras tom confessional", "introducao >= 500 palavras com cena + problema + promessa", "conclusao >= 500 palavras com sintese transformacional e ultima frase memoravel", "vulnerabilidade antes de autoridade", "fechamento pastoral no padrao dos modelos"],
        "final_critique": ["contagem por secao", "profundidade teologica avaliada", "citacoes biblicas verificadas", "versiculos completos quando exigidos", "italico markdown para DOCX Times New Roman verificado", "frases de efeito verificadas", "aplicacoes praticas vs genericas avaliadas", "gates de publicacao com aprovacao ou reprovacao", "conexao biblica auditada por capitulo", "conformidade material com generate-persuasive-ebooks", "arquitetura fixa por capitulo auditada", "engenharia neuroemocional auditada"],
        "cta_subagent": ["ofertas discretas", "ancoras naturais", "riscos de incoerencia documentados"],
        "metadata_kdp": ["7 palavras-chave BR", "descricao 600-1000 chars", "2 categorias KDP Brasil", "preco BRL sugerido"],
        "landing_page": ["CTA claro", "promessa coerente com livro", "sem exagero visual"],
        "bonus_asset": ["minimo 2000 palavras", "tipo definido (guia/devocional/roteiro)", "citacoes NVI com referencia", "valor real ao leitor"],
    }
    return common + stage_specific.get(stage, [])
def infer_stage_ownership(stage: str, *, chapter_name: str | None) -> str:
    if stage == "transcription_correction":
        return "Responsavel por 02_corrigido.txt e pela fidelidade da fonte editorial."
    if stage == "sermon_summary":
        return "Responsavel por 03_resumo_sermao.md."
    if stage == "book_blueprint":
        return "Responsavel por 04_blueprint_ebook.md."
    if stage in {"chapter_writing", "chapter_revision"}:
        chapter_label = chapter_name or "Capitulo alvo"
        return f"Responsavel apenas pelo trecho referente a {chapter_label} em 06_ebook.md, sem reverter outros capitulos."
    if stage == "framing_sections":
        return "Responsavel por Prefacio, Introducao e Conclusao em 06_ebook.md, escritos apenas ao final da redacao."
    if stage == "final_critique":
        return "Responsavel por 05_relatorio_editorial.md."
    if stage == "cta_subagent":
        return "Responsavel apenas por 11_cta_subagent.json."
    if stage == "metadata_kdp":
        return "Responsavel por 09_metadata_kdp.json."
    if stage == "landing_page":
        return "Responsavel por 07_landing.html."
    if stage == "bonus_asset":
        return "Responsavel por 08_bonus.md."
    return "Responsavel apenas pelo artefato-alvo da etapa."


def resolve_execution_profile(metadata: dict[str, Any], profile_override: str | None) -> str:
    selected = (profile_override or metadata.get("execution_profile") or DEFAULT_EXECUTION_PROFILE).strip().lower()
    return selected if selected in SUPPORTED_PROFILES else DEFAULT_EXECUTION_PROFILE


def apply_profile_reasoning(base: str, profile: str) -> str:
    if profile != "economico":
        return base
    if base == "high":
        return "medium"
    if base == "medium":
        return "low"
    return base


def build_checkpoint(stage: str, profile: str) -> dict[str, str]:
    if stage == "cta_subagent":
        return {"type": "select"}
    if stage in {"chapter_writing", "chapter_revision", "metadata_kdp", "landing_page", "bonus_asset"}:
        return {"type": "skip"}
    if profile == "economico" and stage == "transcription_correction":
        return {"type": "skip"}
    return {"type": "approve"}


def max_feedback_cycles_for_profile(profile: str) -> int:
    return 3 if profile == "premium" else 1


def ensure_run_tracking(workspace: Path, metadata: dict[str, Any], profile: str) -> dict[str, Path]:
    run_id = str(metadata.get("run_id") or "")
    if not run_id:
        run_id = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:6]
        metadata["run_id"] = run_id
        metadata["execution_profile"] = profile
        (workspace / "manifest.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    runs_root = workspace / "runs" / run_id
    runs_root.mkdir(parents=True, exist_ok=True)
    state_path = runs_root / "state.json"
    events_path = runs_root / "events.jsonl"
    if not state_path.exists():
        state_payload = {
            "run_id": run_id,
            "page_id": metadata.get("page_id"),
            "execution_profile": profile,
            "ia_agente": detect_runtime_agent(),
            "status": "running",
            "stage_current": "",
            "started_at": datetime.now().isoformat(),
            "ended_at": "",
            "error": "",
        }
        state_path.write_text(json.dumps(state_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if not events_path.exists():
        events_path.write_text("", encoding="utf-8")
    return {"run_dir": runs_root, "state_path": state_path, "events_path": events_path}


def record_run_event(events_path: Path, *, event_type: str, details: dict[str, Any]) -> None:
    event = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "details": details,
    }
    with events_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def update_run_state(
    state_path: Path,
    *,
    status: str,
    stage: str,
    profile: str,
    error: str = "",
) -> None:
    payload = json.loads(state_path.read_text(encoding="utf-8-sig"))
    payload["status"] = status
    payload["stage_current"] = stage
    payload["execution_profile"] = profile
    payload["ia_agente"] = detect_runtime_agent()
    if error:
        payload["error"] = error
    if status in {"completed", "failed", "aborted"}:
        payload["ended_at"] = datetime.now().isoformat()
    state_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def list_runs(workspace_root: Path, *, page_id: str | None, limit: int) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for manifest_path in workspace_root.glob("*/manifest.json"):
        workspace = manifest_path.parent
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        if page_id and manifest.get("page_id") != page_id:
            continue
        for state_path in sorted((workspace / "runs").glob("*/state.json"), reverse=True):
            try:
                state = json.loads(state_path.read_text(encoding="utf-8-sig"))
            except Exception:
                continue
            started = state.get("started_at") or ""
            ended = state.get("ended_at") or ""
            entries.append(
                {
                    "workspace": str(workspace),
                    "run_id": state.get("run_id") or state_path.parent.name,
                    "page_id": state.get("page_id") or manifest.get("page_id"),
                    "status": state.get("status") or "unknown",
                    "stage_current": state.get("stage_current") or "",
                    "execution_profile": state.get("execution_profile") or manifest.get("execution_profile") or DEFAULT_EXECUTION_PROFILE,
                    "ia_agente": state.get("ia_agente") or "",
                    "started_at": started,
                    "ended_at": ended,
                    "duration_seconds": duration_seconds(started, ended),
                }
            )
    entries.sort(key=lambda item: (item.get("started_at") or ""), reverse=True)
    return {"count": len(entries), "items": entries[: max(1, limit)]}


def duration_seconds(started: str, ended: str) -> int:
    if not started or not ended:
        return 0
    try:
        return max(0, int((datetime.fromisoformat(ended) - datetime.fromisoformat(started)).total_seconds()))
    except Exception:
        return 0


def run_healthcheck() -> list[str]:
    issues: list[str] = []
    root = Path(__file__).resolve().parents[1]
    try:
        policy = load_model_routing_policy()
    except Exception as exc:
        return [f"Falha ao carregar model-routing-policy.json: {exc}"]

    for stage in policy.get("stage_order", []):
        if stage not in policy.get("stages", {}):
            issues.append(f"Stage em stage_order sem configuração: {stage}")

    for rel in CRITICAL_SYNC_FILES:
        if not (root / rel).exists():
            issues.append(f"Arquivo crítico ausente: {rel}")

    for rel in ("skill-version.json", "README.md", "SKILL.md", "references/master-conformity-checklist.md"):
        if not (root / rel).exists():
            issues.append(f"Arquivo obrigatório ausente para governança: {rel}")

    required_update_fields = {"Nome_Ebook", "Relatorio_Editorial", "IA Agente", "Status"}
    update_keys = set(build_push_updates_preview().keys())
    missing = sorted(required_update_fields - update_keys)
    if missing:
        issues.append(f"Campos mínimos ausentes no payload de push: {', '.join(missing)}")

    return issues


def build_push_updates_preview() -> dict[str, Any]:
    return {
        "Nome_Ebook": "",
        "Data_Criacao": "",
        "Palavras_Ebook": 0,
        "Landing_HTML": "",
        "Metadata_KDP": "",
        "Relatorio_CTA": "",
        "Resumo_Sermao": "",
        "Blueprint_Ebook": "",
        "Relatorio_Editorial": "",
        "Score_Qualidade": 0,
        "Falhas_QA": "",
        "IA Agente": "",
        "Status": "",
    }


def sync_skills() -> dict[str, Any]:
    root = Path(__file__).resolve().parents[1]
    targets = skill_target_map()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    synced: list[dict[str, Any]] = []

    # Sync only the essential directories/files to avoid long copy times.
    sync_items = [
        "SKILL.md",
        "README.md",
        "requirements.txt",
        "config.example.json",
        "agents",
        "scripts",
        "references",
        "tests",
        "skill-version.json",
        "integrations/README.md",
        "integrations/claude-agent-wrapper.md",
        "integrations/cursor-agent-wrapper.md",
        "integrations/gemini-agent-wrapper.md",
        "integrations/windsurf-agent-wrapper.md",
        "integrations/deployment-notes.md",
    ]

    for alias, target in targets.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        for item in sync_items:
            src = root / item
            dst = target / item
            if not src.exists():
                continue
            if src.is_dir():
                shutil.copytree(
                    src,
                    dst,
                    dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns(
                        "__pycache__",
                        "*.pyc",
                        "*.pyo",
                        ".pytest_cache",
                        "test-runs",
                        "output",
                        "runs",
                        "stage-runs",
                        "chapter-packets",
                    ),
                )
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        synced.append(
            {
                "alias": alias,
                "target": str(target),
                "hashes": compute_critical_hashes(target),
            }
        )

    report = {
        "synced_at": datetime.now().isoformat(),
        "backup_id": "",
        "source": str(root),
        "critical_files": CRITICAL_SYNC_FILES,
        "targets": synced,
    }
    report_path = root / "integrations" / "sync-report-latest.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def rollback_sync(backup_id: str | None) -> dict[str, Any]:
    root = Path(__file__).resolve().parents[1]
    backups_dir = root / "integrations" / "backups"
    if not backups_dir.exists():
        raise RuntimeError("Nenhum backup de sync encontrado.")
    selected = backup_id
    if not selected:
        candidates = sorted([item.name for item in backups_dir.iterdir() if item.is_dir()], reverse=True)
        if not candidates:
            raise RuntimeError("Nenhum backup de sync encontrado.")
        selected = candidates[0]
    backup_root = backups_dir / selected
    if not backup_root.exists():
        raise RuntimeError(f"Backup não encontrado: {selected}")

    target_map = skill_target_map()

    restored: list[str] = []
    for alias, target in target_map.items():
        source = backup_root / alias
        if not source.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target, dirs_exist_ok=True)
        restored.append(str(target))

    return {"backup_id": selected, "restored_targets": restored}


def compute_critical_hashes(base_dir: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for rel in CRITICAL_SYNC_FILES:
        path = base_dir / rel
        if not path.exists():
            hashes[rel] = "missing"
            continue
        hashes[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def warn_version_drift() -> None:
    try:
        root = Path(__file__).resolve().parents[1]
        base_hashes = compute_critical_hashes(root)
        targets = list(skill_target_map().values())
        drift = []
        for target in targets:
            if not target.exists():
                continue
            target_hashes = compute_critical_hashes(target)
            if target_hashes != base_hashes:
                drift.append(str(target))
        if drift:
            print("WARN: drift detectado em instalações da skill. Rode `sync-skills` para alinhar.", file=sys.stderr)
            for item in drift:
                print(f"WARN: - {item}", file=sys.stderr)
    except Exception:
        # Warning helper must never block command execution.
        return


def skill_target_map() -> dict[str, Path]:
    user_home = Path.home()
    return {
        "codex": user_home / ".codex" / "skills" / "kdp-notion-agent",
        "claude": user_home / ".claude" / "skills" / "kdp-notion-agent",
        "gemini": user_home / ".gemini" / "skills" / "kdp-notion-agent",
        "cursor": user_home / ".cursor" / "skills" / "kdp-notion-agent",
        "windsurf": user_home / ".windsurf" / "skills" / "kdp-notion-agent",
    }


def list_orchestration_chapters(package: Any) -> list[str]:
    ebook_text = package.files["ebook_markdown"].read_text(encoding="utf-8-sig")
    chapter_names: list[str] = []
    for line in ebook_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("## "):
            continue
        heading = stripped[3:].strip()
        lowered = heading.casefold()
        if lowered.startswith("capítulo") or lowered.startswith("capitulo"):
            chapter_names.append(heading)
    if chapter_names:
        return chapter_names

    blueprint_text = package.files["ebook_blueprint"].read_text(encoding="utf-8-sig")
    for line in blueprint_text.splitlines():
        stripped = line.strip().lstrip("-").strip()
        lowered = stripped.casefold()
        if lowered.startswith("capítulo") or lowered.startswith("capitulo"):
            chapter_names.append(stripped.split(":", 1)[0].strip())
    return chapter_names or ["Capítulo 1"]


def build_chapter_packet(package: Any, *, chapter_name: str) -> str:
    summary = read_excerpt(package.files["sermon_summary"], max_chars=3000)
    blueprint = package.files["ebook_blueprint"].read_text(encoding="utf-8-sig")
    chapter_goal = find_chapter_goal(blueprint, chapter_name)
    chapter_role = chapter_role_spec(chapter_name)
    corrected = package.files["corrected_transcription"].read_text(encoding="utf-8-sig")
    source_excerpt = select_relevant_paragraphs(corrected, chapter_name=chapter_name, chapter_goal=chapter_goal, limit=10)
    return (
        f"# Chapter Packet\n\n"
        f"## REGRA DE OURO — FIDELIDADE AO SERMAO\n\n"
        f"Este capitulo deve ser construido EXCLUSIVAMENTE a partir do conteudo presente nos "
        f"trechos da transcricao e no resumo do sermao abaixo. "
        f"NAO invente argumentos, historias, analogias ou aplicacoes que o pregador nao mencionou. "
        f"Se precisar expandir, aprofunde o que ja esta no sermao. Zero divagacao.\n\n"
        f"## Capitulo alvo\n\n{chapter_name}\n\n"
        f"## Papel fixo do capitulo\n\n{chapter_role}\n\n"
        f"## Objetivo do capitulo\n\n{chapter_goal}\n\n"
        f"## Resumo completo do sermão (fonte de autoridade)\n\n{summary}\n\n"
        f"## Trechos relevantes da transcricao corrigida (use como ancoras primarias)\n\n{source_excerpt}\n\n"
        f"## Checklist editorial obrigatorio\n\n"
        f"- Minimo 900 palavras de conteudo real (nao contar titulos)\n"
        f"- Abrir com cena, pergunta ou afirmacao que prenda o leitor\n"
        f"- Desenvolver em pelo menos 3 movimentos distintos de argumento\n"
        f"- Linguagem especifica e concreta derivada do sermao — ZERO cliches genericos\n"
        f"- NENHUMA historia ou ilustracao repetida de outros capitulos\n"
        f"- NENHUM tema que nao esteja presente na transcricao ou no resumo\n"
        f"- Cumprir o papel fixo do numero do capitulo dentro da arquitetura persuasive ebooks\n"
        f"- Ativar risco, conflito, pertencimento, clareza causal e direcao pratica sem soar manipulativo\n"
        f"- Fechar com frase de impacto ou gancho para o proximo capitulo\n"
        f"- PT-BR natural e fluido\n"
    )


def find_chapter_goal(blueprint_text: str, chapter_name: str) -> str:
    lowered = chapter_name.strip().lower()
    for line in blueprint_text.splitlines():
        clean = line.strip().lstrip("-").strip()
        if not clean:
            continue
        if lowered in clean.lower():
            parts = clean.split(":", 1)
            if len(parts) == 2:
                return parts[1].strip()
            return clean
    return "Desenvolver o capitulo com fidelidade ao eixo central do ebook."


def select_relevant_paragraphs(corrected_text: str, *, chapter_name: str, chapter_goal: str, limit: int = 6) -> str:
    keywords = extract_keywords(f"{chapter_name} {chapter_goal}")
    paragraphs = [item.strip() for item in re.split(r"\n\s*\n", corrected_text) if item.strip()]
    scored: list[tuple[int, str]] = []
    for paragraph in paragraphs:
        lowered = paragraph.lower()
        score = sum(lowered.count(keyword) for keyword in keywords)
        if score > 0:
            scored.append((score, paragraph))
    if not scored:
        fallback = paragraphs[:limit]
        return "\n\n".join(fallback) if fallback else "(sem trechos relevantes disponiveis)"
    scored.sort(key=lambda item: (-item[0], len(item[1])))
    selected = [paragraph for _, paragraph in scored[:limit]]
    return "\n\n".join(selected)


def extract_keywords(text: str) -> list[str]:
    raw = re.findall(r"[A-Za-zÀ-ÿ]{4,}", text.lower())
    stopwords = {
        "capitulo",
        "sobre",
        "para",
        "com",
        "este",
        "essa",
        "isso",
        "como",
        "mais",
        "menos",
        "livro",
        "ebook",
        "sermao",
        "capitulo",
    }
    return [word for word in raw if word not in stopwords][:12]


def load_cta_payload(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    payload = normalize_cta_payload(payload)
    payload["__path__"] = str(path)
    return payload


def promote_cta_subagent_output(subagent_path: Path, report_path: Path, *, title: str) -> dict[str, Any]:
    report_payload: dict[str, Any] = {}
    if report_path.exists():
        report_payload = json.loads(report_path.read_text(encoding="utf-8-sig"))

    subagent_payload = load_cta_subagent_payload(subagent_path)
    if not subagent_payload:
        normalized = normalize_cta_payload(
            report_payload or {"tema": title, "promessa_central": "", "produtos": [], "proxima_acao": ""}
        )
        report_path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")
        return normalized

    promoted = {
        "tema": subagent_payload.get("tema") or report_payload.get("tema") or title,
        "promessa_central": subagent_payload.get("promessa_central") or report_payload.get("promessa_central") or "",
        "audiencia": subagent_payload.get("audiencia") or report_payload.get("audiencia") or "",
        "produtos": promote_subagent_products(subagent_payload),
        "proxima_acao": report_payload.get("proxima_acao") or "Inserir apenas CTAs organicamente coerentes com o sermão.",
        "ganchos_editoriais_por_capitulo": subagent_payload.get("ganchos_editoriais_por_capitulo") or [],
        "riscos_de_incoerencia": subagent_payload.get("riscos_de_incoerencia") or [],
        "subagente_origem": {
            "arquivo": subagent_path.name,
            "aplicado_em": datetime.now().isoformat(),
        },
    }

    if report_payload.get("links_inseridos_no_ebook"):
        promoted["links_inseridos_no_ebook"] = report_payload["links_inseridos_no_ebook"]

    normalized = normalize_cta_payload(promoted)
    report_path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")
    return normalized


def load_cta_subagent_payload(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        return {}
    if not any(payload.get(key) for key in ("produtos_sugeridos", "ctas_recomendados", "ganchos_editoriais_por_capitulo")):
        return {}
    return payload


def promote_subagent_products(subagent_payload: dict[str, Any]) -> list[dict[str, Any]]:
    suggested_products = subagent_payload.get("produtos_sugeridos") or []
    recommended_ctas = subagent_payload.get("ctas_recomendados") or []
    promoted: list[dict[str, Any]] = []
    fallback_url = "https://filipeivopereira.com/loja"

    for index, product in enumerate(suggested_products):
        cta = recommended_ctas[index] if index < len(recommended_ctas) and isinstance(recommended_ctas[index], dict) else {}
        promoted.append(
            {
                "nome": str(product.get("nome") or cta.get("produto") or cta.get("nome") or "").strip(),
                "preco": str(product.get("preco") or "").strip(),
                "plataforma": str(product.get("plataforma") or "Loja própria").strip(),
                "link": str(product.get("link") or cta.get("link") or fallback_url).strip(),
                "status": str(product.get("status") or "SUGERIDO").strip(),
                "cta_texto_ebook": str(
                    cta.get("anchor_text") or cta.get("texto_link") or product.get("cta_texto_ebook") or product.get("nome") or ""
                ).strip(),
                "descricao": str(product.get("descricao") or cta.get("frase_contextual") or "").strip(),
                "capitulo_alvo": str(cta.get("capitulo_alvo") or "").strip(),
            }
        )

    if not promoted:
        for cta in recommended_ctas:
            if not isinstance(cta, dict):
                continue
            promoted.append(
                {
                    "nome": str(cta.get("produto") or cta.get("nome") or cta.get("anchor_text") or "Material complementar").strip(),
                    "preco": "",
                    "plataforma": "Loja própria",
                    "link": str(cta.get("link") or fallback_url).strip(),
                    "status": "SUGERIDO",
                    "cta_texto_ebook": str(cta.get("anchor_text") or cta.get("texto_link") or "materiais estudo").strip(),
                    "descricao": str(cta.get("frase_contextual") or "").strip(),
                    "capitulo_alvo": str(cta.get("capitulo_alvo") or "").strip(),
                }
            )

    return promoted[:5]


def inject_cta_links(markdown_text: str, cta_payload: dict[str, Any]) -> str:
    products = cta_payload.get("produtos", [])
    if not products:
        return markdown_text

    selected = products[:5]
    markdown_text = strip_existing_cta_paragraphs(markdown_text)
    sections = markdown_text.split("\n## ")
    existing_markdown = markdown_text
    if len(sections) < 4:
        return markdown_text

    insertion_indexes: list[int] = []
    body_start = 2
    body_end = len(sections) - 1
    available = max(0, body_end - body_start)
    if available == 0:
        return markdown_text
    step = max(1, available // max(1, len(selected)))
    cursor = body_start
    while len(insertion_indexes) < len(selected) and cursor < len(sections):
        insertion_indexes.append(cursor)
        cursor += step

    inserted_links = []
    for idx, product in zip(insertion_indexes, selected):
        link_text = str(product.get("cta_texto_ebook") or product.get("nome") or "materiais de estudo").strip()
        url = str(product.get("link") or "https://filipeivopereira.com/loja").strip()
        link_marker = f"[{link_text}]({url})"
        if link_marker in existing_markdown:
            inserted_links.append({"texto": link_text, "url": url, "produto": str(product.get("nome", ""))})
            continue
        phrase = build_cta_phrase(product, link_text, url)
        if phrase not in sections[idx]:
            sections[idx] = sections[idx].rstrip() + "\n\n" + phrase + "\n"
            inserted_links.append({"texto": link_text, "url": url, "produto": str(product.get("nome", ""))})
            existing_markdown += "\n" + phrase

    cta_payload["links_inseridos_no_ebook"] = inserted_links
    path = cta_payload.get("__path__")
    if path:
        Path(path).write_text(json.dumps({k: v for k, v in cta_payload.items() if k != "__path__"}, ensure_ascii=False, indent=2), encoding="utf-8")
    return "\n## ".join(sections)


def strip_existing_cta_paragraphs(markdown_text: str) -> str:
    cleaned_lines: list[str] = []
    for line in markdown_text.splitlines():
        normalized = line.strip().lower()
        if "filipeivopereira.com/loja" in normalized:
            continue
        cleaned_lines.append(line)
    cleaned_text = "\n".join(cleaned_lines)
    cleaned_text = re.sub(r"\n{3,}", "\n\n", cleaned_text)
    return cleaned_text.strip() + "\n"


def build_cta_phrase(product: dict[str, Any], link_text: str, url: str) -> str:
    name = str(product.get("nome", "")).strip()
    description = str(product.get("descricao", "")).strip()
    intros = [
        "Se você deseja aprofundar este ponto com",
        "Para continuar essa reflexão com",
        "Se quiser avançar neste tema com",
        "Para complementar este capítulo com",
    ]
    intro = intros[abs(hash((name, link_text, url))) % len(intros)]
    if description:
        return f"{intro} [{link_text}]({url}), vale conhecer {name}: {description}."
    return f"{intro} [{link_text}]({url}), vale conhecer {name or link_text}."


def normalize_cta_payload(payload: dict[str, Any]) -> dict[str, Any]:
    tema = str(payload.get("tema") or "este tema").strip()
    products = list(payload.get("produtos") or [])
    defaults = [
        {
            "nome": f"Workbook de {tema}",
            "preco": "",
            "plataforma": "Loja própria",
            "link": "https://filipeivopereira.com/loja",
            "status": "SUGERIDO",
            "cta_texto_ebook": "workbook extras",
            "descricao": "Material prático para aprofundar a mensagem com exercícios e aplicação.",
        },
        {
            "nome": f"Materiais de estudo sobre {tema}",
            "preco": "",
            "plataforma": "Loja própria",
            "link": "https://filipeivopereira.com/loja",
            "status": "SUGERIDO",
            "cta_texto_ebook": "materiais estudo",
            "descricao": "Recursos complementares para continuar a reflexão bíblica do ebook.",
        },
        {
            "nome": "Catálogo bíblico completo",
            "preco": "",
            "plataforma": "Loja própria",
            "link": "https://filipeivopereira.com/loja",
            "status": "SUGERIDO",
            "cta_texto_ebook": "catálogo bíblico",
            "descricao": "Coleção de ebooks e estudos para aprofundamento pastoral e devocional.",
        },
    ]
    existing_keys = {
        (
            str(item.get("nome", "")).strip().lower(),
            str(item.get("cta_texto_ebook", "")).strip().lower(),
        )
        for item in products
    }
    for item in defaults:
        key = (item["nome"].strip().lower(), item["cta_texto_ebook"].strip().lower())
        if len(products) >= 3:
            break
        if key not in existing_keys:
            products.append(item)
            existing_keys.add(key)
    payload["produtos"] = products[:5]
    return payload


def build_cta_delivery_report(path: Path) -> dict[str, Any]:
    payload = normalize_cta_payload(json.loads(path.read_text(encoding="utf-8-sig")))
    payload["quantidade_links_inseridos"] = len(payload.get("links_inseridos_no_ebook", []))
    return payload


def safe_slug(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-") or "ebook"


def chapter_draft_path(workspace: Path, chapter_name: str) -> Path:
    """Return the isolated draft file path for a single chapter."""
    drafts_dir = workspace / "chapter-drafts"
    drafts_dir.mkdir(exist_ok=True)
    return drafts_dir / f"{safe_slug(chapter_name)}.md"


def consolidate_chapters(workspace: Path) -> Path:
    """Merge all chapter-drafts/{slug}.md into 06_ebook.md, preserving blueprint order."""
    package = build_final_package(workspace)
    chapters = list_orchestration_chapters(package)
    title = package.metadata.get("title", "Ebook")
    ebook_path = package.files["ebook_markdown"]
    parts: list[str] = [f"# {title}\n"]
    for chapter_name in chapters:
        draft = chapter_draft_path(workspace, chapter_name)
        if draft.exists():
            content = draft.read_text(encoding="utf-8-sig").strip()
            parts.append(content)
        else:
            parts.append(f"## {chapter_name}\n\n<!-- rascunho ausente: {draft.name} -->")
    ebook_path.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    return ebook_path


def _write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def _configure_stdio() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


if __name__ == "__main__":
    raise SystemExit(main())
