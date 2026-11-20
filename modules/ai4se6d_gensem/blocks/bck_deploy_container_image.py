"""Slide — Image and container; a Dockerfile (CalcApp's, simplified) (CCSET16, edition 2)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Image and container styles."""
    heading = s.project.titles.heading
    label = s.project.titles.label
    body = s.project.titles.body
    caption = Style.create(s.project.titles.caption + s.center_txt, "container_caption")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_DOCKERFILE = (
    "# stage 1: build\n"
    "FROM node:22-alpine AS build\n"
    "WORKDIR /app\n"
    "COPY package.json package-lock.json ./\n"
    "RUN npm ci\n"
    "COPY . .\n"
    "RUN npm run test:run && npm run build\n"
    "# stage 2: run\n"
    "FROM nginx:1.28-alpine\n"
    "COPY --from=build /app/dist /usr/share/nginx/html\n"
    "EXPOSE 3000\n"
    "HEALTHCHECK CMD wget -q -O /dev/null http://127.0.0.1:3000/"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(60):
            st_write(bs.heading, "Image and Container", tag=t.div, toc_lvl="+1", label="Image, container, Dockerfile")
            with st_grid(cols="44% 54%", gap="24px") as g:
                with g.cell():
                    with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                        with l.item(): st_write(bs.body, (bs.label, "Image"), ": a frozen package — system, runtime, "
                                                "your built app")
                        with l.item(): st_write(bs.body, (bs.label, "Container"), ": one running copy of an image, "
                                                "isolated; restart it and it starts fresh")
                        with l.item(): st_write(bs.body, (bs.label, "Dockerfile"), ": the recipe of the image, "
                                                "versioned with the code")
                        with l.item(): st_write(bs.body, "Two stages: build with Node, run with a small web server — "
                                                "no source code, no Node in production")
                with g.cell():
                    st_code(s.none, code=_DOCKERFILE, language="dockerfile", line_numbers=False)
                    st_write(bs.caption, "CalcApp's Dockerfile, simplified — the starter ships it, tested.", tag=t.div)
            st_write(bs.source, cite("merkel-docker2014"), tag=t.div)
