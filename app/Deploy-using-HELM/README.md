# Helm

The apps deployed using kubernetes before, here are deployed using Helm.

## Basic Commands
```bash
helm install app1 webapp1/
helm upgrade app1 webapp1/ --values webapp1/values.yaml 
helm uninstall app1
```

## Useful Commands
```bash
helm get notes app1
helm get manifest app1
helm history app1
helm rollback app1 1
helm uninstall app1 --keep-history
```
