# csv-blueprint
A Python CSV validation tool that validates the records in a CSV file using a YAML schema. 

Given a CSV file like this:

| full_name     | age |
| ------------- | --- |
| taiye christy | 45  |
| kobbie mainoo | 19  |

You can validate it with a schema like this:

```yaml
name: 'people file'

columns:
- name: full_name
  rules:
    not_empty: true
    is_trimmed: true
    is_lowercase: true
    is_uuid: true

- name: age
  rules:
    is_int: true
    num_min: 0
```

The v1 is compatible and based on the most important features in https://github.com/JBZoo/CSV-Blueprint which is written in PHP. Doing validation with the PHP version introduced considerable architectural changes to `our` data pipelines making this port required.

## Installation

```sh
pip install csv-blueprint
```

## Usage
The library include scripts that can be used from a command terminal, it can also be imported and used in code. To use it from the command line

```sh
validate-csv --csv path-to-csv-file --schema path-to-yaml-schema
```

## Rules

The available rules are included in the `examples/rules.yaml` file.
