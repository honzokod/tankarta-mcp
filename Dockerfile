FROM registry.access.redhat.com/ubi10/python-312-minimal

ENV TANKARTA_URL=example.com
ENV MCPO_API=

ADD pyproject.toml uv.lock README.md /app/
ADD src /app/src/

WORKDIR /app

RUN pip install -U pip uv && \
    uv tool install .

ENTRYPOINT ["uvx", "mcpo", "--port", "8000", "--api-key", "${MCPO_API}}", "--", "tankarta-mcp"]
