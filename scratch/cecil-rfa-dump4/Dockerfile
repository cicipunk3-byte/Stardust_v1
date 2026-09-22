# =====================================================================
# STAGE 1: Compilation and Dependency Assembly
# =====================================================================
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU compilation layer natively to optimize image footprint
RUN pip install --no-cache-dir --user torch --index-url https://pytorch.org \
    && pip install --no-cache-dir --user numpy

# =====================================================================
# STAGE 2: Secure Production Standalone Container
# =====================================================================
FROM python:3.11-slim AS production

WORKDIR /workspace

# Copy local wheels and binary assets compiled in builder layer
COPY --from=builder /root/.local /root/.local
COPY rfa_production_pipeline.py /workspace/rfa_production_pipeline.py

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Expose standard workspace API communications port
EXPOSE 8080

ENTRYPOINT ["python", "rfa_production_pipeline.py"]
