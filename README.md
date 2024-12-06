# Utils

Utilities to automate/simplify some tasks

## 1. Config Utilities

### 1.1 Compare:
Compares two config files, where configurations are defined as CONFIG_**.

```bash
$> cd ./config-utilities
$> nix-shell #For NixOS only
$> python ./tools/config-compare.py <config-file1> <config-file2>
$> python ./tools/config-compare.py ./kernel-configs/kernel-6.12-hardening.config ./kernel-configs/ghaf-host.config  #Example
```

### 1.2 Describe Linux Config:
Gives "what about" information of any valid Linux configuration.
```bash
$> cd ./config-utilities
$> nix-shell #For NixOS only
$> python ./tools/describe_me.py <config>
$> python ./tools/describe_me.py CONFIG_BUG #Example
```

### 1.3 Detailed comparision:
Compares two Linux config files and generates detailed report in form of Markdown table.

```bash
$> cd ./config-utilities
$> nix-shell #For NixOS only
$> python ./tools/compare_and_generate_md.py <base_config-file> <target_config_file>
$> python ./tools/compare_and_generate_md.py ./kernel-configs/kernel-6.12-hardening.config ./kernel-configs/ghaf-host.config  #Example
```


#Reports:
Config comparision report of ghaf-host kernel and Linux-6.12 hardening config is available here:

[Comparision Report](./config-utilities/report/configs.md)

**Base config:** [Linux-6.12 hardening config](https://github.com/torvalds/linux/blob/v6.12/kernel/configs/hardening.config)

**Target config:** ghaf-host-24.09-04-01bb7e379cc581525fc2952744595a26bb7d21c8 - Linux-6.6.62
                (Config captured from /proc/config.gz of ghaf-host)
