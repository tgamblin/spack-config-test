#!/usr/bin/env spack-python

import sys

import spack.config
import spack.schema
import spack.util.spack_yaml as syaml

scopes = reversed([
    spack.config.SingleFileScope("a", "a.yaml", spack.schema.config.schema),
    spack.config.SingleFileScope("b", "b.yaml", spack.schema.config.schema),
    spack.config.SingleFileScope("c", "c.yaml", spack.schema.config.schema),
    spack.config.SingleFileScope("d", "d.yaml", spack.schema.config.schema),
])

config = spack.config.Configuration()
for scope in scopes:
    config.push_scope(scope)

syaml.dump_config({"config": config.get("config")}, sys.stdout, blame=True)
