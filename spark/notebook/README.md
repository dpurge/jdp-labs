# Spark lab: Notebook

```pwsh
docker build . -t jdpspark
docker run --rm --volume ${PWD}/work-dir:/opt/spark/work-dir --volume ${PWD}/data:/opt/spark/data -p 8888:8888 --name spark -e GITHUB_READ_TOKEN=$env:GITHUB_READ_TOKEN -d jdpspark
```
