from streamtex import *  # noqa: F403
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    title = s.project.titles.slide_title + s.center_txt
    subtitle = s.project.titles.subtitle
    content = s.project.titles.body
    emphasis = s.project.titles.body + s.bold + s.project.colors.primary
    mcp = s.project.titles.body + s.bold + s.project.colors.critical
    quote = s.project.titles.body + ns("font-style: italic; padding-left: 24px; border-left: 3px solid #7AB8F5;")
    key = s.project.titles.body + s.bold


bs = BlockStyles


def build():
    st_write(bs.title, "Case Study — Maria's WebShop", tag=t.div, toc_lvl="2")
    st_space(size=2)

    # ── Context ──
    st_write(bs.subtitle, "Context", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    st_write(
        bs.content,
        "Maria runs a brick-and-mortar Italian delicatessen managed with Odoo ERP. "
        "She wants to launch an online shop for premium Italian products "
        "(artisan pasta, olive oil, charcuterie, wines) with delivery to France and Belgium. "
        "She needs a complete requirements document — functional, non-functional, "
        "and infrastructure — with a cloud deployment proposal on Hetzner for up to 2000 concurrent users.",
    )
    st_space(size=2)

    # ── Maria's Prompt ──
    st_write(bs.subtitle, "Maria's Prompt", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    with st_block(bs.quote):
        st_write(
            "Help me write the full requirements document for my Italian food webshop. "
            "I want to deliver to France and Belgium, support up to 2000 concurrent users, "
            "and deploy on Hetzner cloud. My shop runs on Odoo — use its data to size things correctly.",
        )
    st_space(size=2)

    # ── What the Agent Will Produce ──
    st_write(bs.subtitle, "Expected Output", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    st_write(bs.content, "A structured requirements document with 5 sections:")
    with st_list(list_type=lt.ordered, li_style=bs.content) as l:
        with l.item():
            st_write((bs.key, "Context & Objectives"), (bs.content, " — Maria's business, goals, scope"))
        with l.item():
            st_write((bs.key, "Functional Requirements"), (bs.content, " — catalog, cart, payment, delivery, traceability, age verification"))
        with l.item():
            st_write((bs.key, "Non-Functional Requirements"), (bs.content, " — performance, GDPR, availability, accessibility, SEO"))
        with l.item():
            st_write((bs.key, "Deployment Architecture"), (bs.content, " — Hetzner infrastructure sized from Odoo data"))
        with l.item():
            st_write((bs.key, "Budget Estimate"), (bs.content, " — monthly cost based on Hetzner pricing"))
    st_space(size=2)

    # ── The Cast ──
    st_write(bs.subtitle, "The Agents", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    agents = [
        ("Main Agent (Opus)", "Orchestrates the whole process: collects data, delegates, assembles, delivers."),
        ("Functional Analyst (Haiku)", "Researches functional requirements for food e-commerce: catalog features, "
         "payment methods, delivery modes, regulatory compliance."),
        ("Non-Functional Analyst (Haiku)", "Researches NFRs: performance targets, GDPR, "
         "availability SLA, accessibility standards, SEO."),
        ("Cloud Architect (Opus)", "Sizes the Hetzner infrastructure. Spawns 2 sub-sub-agents:"),
    ]
    for name, desc in agents:
        st_write((bs.emphasis, name), (bs.content, f" — {desc}"))
        st_space(size=1)

    sub_agents = [
        ("C1 — Volumetry Analyst", "queries Odoo MCP for business metrics (orders/day, peaks, catalog size) "
         "and derives CPU/RAM/storage needs."),
        ("C2 — Pricing Analyst", "queries Hetzner API MCP for server types, load balancer options, "
         "and volume pricing to build a budget proposal."),
    ]
    with st_list(list_type=lt.unordered, li_style=bs.content) as l:
        for name, desc in sub_agents:
            with l.item():
                st_write((bs.mcp, name), (bs.content, f" — {desc}"))
    st_space(size=2)

    # ── MCP Tools Involved ──
    st_write(bs.subtitle, "MCP Connections", tag=t.div, toc_lvl="+1")
    st_space(size=1)

    with st_grid(
        cols="1fr 1fr 2fr",
        grid_style=ns("gap: 0; border: 1px solid #444; border-radius: 8px; overflow: hidden;"),
        cell_styles=[bs.key] * 3,
    ):
        st_write("MCP Server")
        st_write("Transport")
        st_write("Data Provided")

    mcp_data = [
        ("Odoo ERP", "Local (stdio)", "150 orders/day, 1200 products, 45K€/mo, peak ×3 in Dec, avg 3.2kg"),
        ("Hetzner API", "Remote (SSE)", "CPX31: 4vCPU 8GB 9.29€/mo, LB: 5.49€/mo, Vol 100GB: 4.40€/mo"),
        ("Gmail", "Remote (SSE)", "Send requirements draft to Maria for review"),
        ("Calendar", "Remote (SSE)", "Schedule review meeting with Maria and tech partner"),
    ]
    for server, transport, data in mcp_data:
        with st_grid(
            cols="1fr 1fr 2fr",
            grid_style=ns("gap: 0; border-left: 1px solid #444; border-right: 1px solid #444; border-bottom: 1px solid #444;"),
            cell_styles=[s.small] * 3,
        ):
            st_write(bs.key, server)
            st_write(transport)
            st_write(data)
