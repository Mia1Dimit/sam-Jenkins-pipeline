# Use the official Jenkins base image
FROM jenkins/jenkins:lts

# Install necessary dependencies
USER root
RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    && apt-get clean

# Switch back to the jenkins user
USER jenkins

# Expose Jenkins port
EXPOSE 8080
