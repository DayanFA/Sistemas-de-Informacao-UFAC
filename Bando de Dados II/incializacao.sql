CREATE DATABASE tpch;
USE tpch;

CREATE TABLE tpch.part
(
    p_partkey       DECIMAL(10, 0),
    p_name          VARCHAR(55),
    p_mfgr          CHAR(25),
    p_brand         CHAR(10),
    p_type          VARCHAR(25),
    p_size          INTEGER,
    p_container     CHAR(10),
    p_retailprice   DECIMAL,
    p_comment       VARCHAR(23)
);
CREATE TABLE tpch.supplier
(
    s_suppkey     DECIMAL(10, 0),
    s_name        CHAR(25),
    s_address     VARCHAR(40),
    s_nationkey   DECIMAL(10, 0),
    s_phone       CHAR(15),
    s_acctbal     DECIMAL,
    s_comment     VARCHAR(101)
);
CREATE TABLE tpch.partsupp
(
    ps_partkey      DECIMAL(10, 0),
    ps_suppkey      DECIMAL(10, 0),
    ps_availqty     INTEGER,
    ps_supplycost   DECIMAL,
    ps_comment      VARCHAR(199)
);
CREATE TABLE tpch.customer
(
    c_custkey      DECIMAL(10, 0),
    c_name         VARCHAR(25),
    c_address      VARCHAR(40),
    c_nationkey    DECIMAL(10, 0),
    c_phone        CHAR(15),
    c_acctbal      DECIMAL,
    c_mktsegment   CHAR(10),
    c_comment      VARCHAR(117)
);
CREATE TABLE tpch.orders
(
    o_orderkey        DECIMAL(10, 0),
    o_custkey         DECIMAL(10, 0),
    o_orderstatus     CHAR(1),
    o_totalprice      DECIMAL,
    o_orderdate       CHAR(10),
    o_orderpriority   CHAR(15),
    o_clerk           CHAR(15),
    o_shippriority    INTEGER,
    o_comment         VARCHAR(79)
);
CREATE TABLE tpch.lineitem
(
    l_orderkey        DECIMAL(10, 0),
    l_partkey         DECIMAL(10, 0),
    l_suppkey         DECIMAL(10, 0),
    l_linenumber      INTEGER,
    l_quantity        DECIMAL,
    l_extendedprice   DECIMAL,
    l_discount        DECIMAL,
    l_tax             DECIMAL,
    l_returnflag      CHAR(1),
    l_linestatus      CHAR(1),
    l_shipdate        CHAR(10),
    l_commitdate      CHAR(10),
    l_receiptdate     CHAR(10),
    l_shipinstruct    CHAR(25),
    l_shipmode        CHAR(10),
    l_comment         VARCHAR(44)
);
CREATE TABLE tpch.nation
(
    n_nationkey   DECIMAL(10, 0),
    n_name        CHAR(25),
    n_regionkey   DECIMAL(10, 0),
    n_comment     VARCHAR(152)
);
CREATE TABLE tpch.region
(
    r_regionkey   DECIMAL(10, 0),
    r_name        CHAR(25),
    r_comment     VARCHAR(152)
);



