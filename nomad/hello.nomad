job "hello" {
  datacenters = ["dc1"]
  type        = "service"

  group "app" {
    task "hello" {
      driver = "docker"

      config {
        image      = "localhost:5000/hello-devops:latest"
        force_pull = false
      }

      resources {
        cpu    = 100
        memory = 128
      }
    }
  }
}
