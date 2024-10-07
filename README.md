# Reddit-metric-analysis

You'll see that in the `docker-compose.yml` file i didn't include all the services and images to pull, that's because I installed them locally on my machine and not as images. If it's not your case, then each service should be looking like this:

```yaml
  zookeeper:
    image: wurstmeister/zookeeper:3.4.6
    ports:
      - "2181:2181"
    pull_policy: "never"
```
The `pull_policy: "never"` if you already got the on your machine as images and don't want them to be pulled by mistake, if not feel free to remove tis parameter