from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
    Index,
)

from systems.db_con import Base


class FetcherSettings(Base):
    __tablename__ = "fetcher_settings"

    id = Column(Integer, primary_key=True)
    logging_mode = Column(Integer)
    crawling_speed_factor = Column(Float)
    default_crawl_delay = Column(Integer)
    parallel_process = Column(Integer)
    iterations = Column(Integer)
    fqdn_amount = Column(Integer)
    url_amount = Column(Integer)
    long_term_mode = Column(String)
    short_term_mode = Column(String)
    min_links_per_page = Column(Integer)
    max_links_per_page = Column(Integer)
    lpp_distribution_type = Column(String)
    internal_vs_external_threshold = Column(Float)
    new_vs_existing_threshold = Column(Float)


class FqdnFrontier(Base):
    __tablename__ = "fqdn_frontiers"

    fqdn_hash = Column(String)
    fqdn = Column(String, primary_key=True, index=True)
    tld = Column(String, index=True)
    fqdn_last_ipv4 = Column(String)
    fqdn_last_ipv6 = Column(String)
    fqdn_url_count = Column(Integer)
    fqdn_pagerank = Column(Float)
    fqdn_crawl_delay = Column(Integer)


class UrlFrontier(Base):
    __tablename__ = "url_frontiers"

    fqdn = Column(String, ForeignKey("fqdn_frontiers.fqdn"))
    url = Column(String, primary_key=True, index=True)
    url_discovery_date = Column(DateTime)
    url_last_visited = Column(DateTime)
    url_blacklisted = Column(Boolean)
    url_bot_excluded = Column(Boolean)
