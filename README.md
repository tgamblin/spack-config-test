# Spack config tests

Simple test script and some YAML files for playing around with
[Spack](https://github.com/spack/spack) config file merging.

Usgae:

First, put `spack-python` in your `PATH`. Then:

```yaml
> ./config-test.py
---       config:
a.yaml:2    data:
a.yaml:3      merged:
a.yaml:4      - a
a.yaml:5      - b
a.yaml:6      - c
b.yaml:4      - d
b.yaml:5      - e
b.yaml:6      - f
a.yaml:7      overwritten: this clobbers a list
c.yaml:3      more:
c.yaml:4      - j
c.yaml:5      - k
c.yaml:6      - l
d.yaml:4      - m
d.yaml:5      - n
d.yaml:6      - o
```

Play with the YAML files to see how lists, dicts, and scalars are merged.
