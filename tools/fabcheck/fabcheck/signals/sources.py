"""Fabricated-source signals. Format checks only; resolution is out of scope."""
import re
from dataclasses import dataclass, field

# Branded-source pattern: "The Tao of Agency (2026)", "Dao: The Art of the Long Game (2026)"
# This was the dominant fabrication class in the CCS doc (5 for 5).
BRANDED_SOURCE = re.compile(
    r"\b((?:The|A)\s+[A-Z][\w'-]+(?:\s+of\s+[A-Z][\w'-]+)+)\s*\((\d{4})\)"
    r"|\b([A-Z][\w'-]+(?::\s*[A-Z][\w' -]+)+)\s*\((\d{4})\)"
)

# Bracketed placeholder organizations: "[Open Secure AI Alliance]", "[WAICO]"
BRACKETED_ORG = re.compile(r"\[\[?([A-Z][\w\s-]{3,60})\]\]?")

DOI = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV = re.compile(r"arXiv:?\s*(\d{4}\.\d{4,5})(v\d+)?", re.IGNORECASE)

CURRENT_YEAR = 2026


@dataclass
class Finding:
    kind: str
    detail: str
    excerpt: str
    severity: str  # "flag" | "warn" | "info"


@dataclass
class SourceReport:
    findings: list = field(default_factory=list)

    def add(self, kind, detail, excerpt, severity):
        self.findings.append(Finding(kind, detail, excerpt, severity))


def check_years(text, report):
    for m in BRANDED_SOURCE.finditer(text):
        year = int(m.group(2) or m.group(4))
        title = m.group(1) or m.group(3)
        # Title-plus-year branded citations were the fabrication signature in
        # the CCS doc (5/5 invented). Always at least a warning.
        if year > CURRENT_YEAR:
            report.add("future-dated source",
                       f"'{title}' dated {year}, which has not happened",
                       m.group(0), "flag")
        elif year < 1900:
            report.add("implausible year", f"'{title}' dated {year}",
                       m.group(0), "warn")
        else:
            report.add("branded source citation",
                       f"'{title}' ({year}): verify this exists before it goes public",
                       m.group(0), "warn")


def check_bracketed_orgs(text, report):
    for m in BRACKETED_ORG.finditer(text):
        report.add("placeholder source",
                   "bracketed organization name, never seen a real citation do this",
                   m.group(0), "flag")


def check_ids(text, report):
    # Format sanity only. A well-formed DOI proves nothing.
    for m in DOI.finditer(text):
        report.add("doi present", "format plausible, unverified", m.group(0), "info")
    for m in ARXIV.finditer(text):
        # arXiv ids are YYMM.number: 2308 = 2023, August.
        yymm = m.group(1).split(".")[0]
        if len(yymm) == 4:
            month = int(yymm[2:4])
            if not (1 <= month <= 12):
                report.add("malformed arXiv id", "month field out of range",
                           m.group(0), "warn")


def check_sources(text):
    report = SourceReport()
    check_years(text, report)
    check_bracketed_orgs(text, report)
    check_ids(text, report)
    return report
