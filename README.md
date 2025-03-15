# Sarvam Iteration 1

Sarvam is a chat application powered by a Large Language Model (LLM) designed to provide dynamic, context-aware conversations. Built with production-readiness in mind, Sarvam lays the groundwork for scaling to support 10,000+ users, while demonstrating best practices in system design, inference optimization, and modular architecture.

---

## Table of Contents

- [Overview](#overview)
- [Core Functionality](#core-functionality)
- [Overall Approach and Design Philosophy](#overall-approach-and-design-philosophy)
- [System Design and Scalability](#system-design-and-scalability)
- [Inference Optimization](#inference-optimization)
- [Key Technical Decisions](#key-technical-decisions)
- [Getting Started](#getting-started)

---

## Overview

Sarvam is a prototype chat application where users interact with an LLM through a friendly chat interface. The application maintains conversation history to provide context and enhance user interactions. The primary goal is to establish a solid foundation that can evolve into a highly scalable system capable of serving over 10,000 concurrent users.
Kindly note that this is a basic implementation of the required chatbot and might not meet expectations. But this is what I could come up with, given the limited time, including Holi holidays. This might not meet expectations but I hope will reflect my commitment to the project, having taken up this entirely new task and worked through it during holidays.
---

## Core Functionality

- **Chat Interface:** A responsive and user-friendly web interface that allows users to send and receive messages from the chatbot.
- **LLM-Powered Conversations:** Integration with a Large Language Model (e.g., OpenAI, Anthropic, Llama) to generate context-aware responses.
- **Conversation History:** Preservation of session context to improve conversational relevance.
- **Scalability:** Architectural choices made with future scalability in mind, ensuring the platform can handle significant user loads.

---

## Overall Approach and Design Philosophy

### Design Philosophy

- **Modularity:** Each component of the system (chat interface, LLM service, session management, logging) is designed as an independent module, allowing for easier updates and maintenance.
- **Scalability:** The design prioritizes scalability through distributed systems, load balancing, and robust caching strategies. The architecture is prepared to scale horizontally as user demand increases.
- **Production-Readiness:** Emphasis on logging, monitoring, fault tolerance, and graceful degradation to ensure high availability in production environments.
- **User Experience:** A commitment to delivering a seamless, responsive, and engaging user experience by leveraging modern UI/UX practices and efficient backend processing.

---

## System Design and Scalability

### Architecture Overview

- **Microservices Architecture:**  
  Decompose the system into dedicated microservices:
  - **Chat Interface Service:** Handles user interactions and message routing.
  - **LLM Inference Service:** Manages requests to the LLM and returns responses.
  - **Session Management Service:** Maintains user session data and conversation histories.
  - **Logging & Monitoring Service:** Tracks performance, error reporting, and system health.

- **Load Balancing:**  
  Deploy load balancers (e.g., NGINX, HAProxy) in front of the services to distribute incoming requests evenly across multiple instances.

- **Database and Storage:**  
  Utilize a robust database system (SQL like PostgreSQL or NoSQL like MongoDB) for storing user data and conversation histories. Consider distributed databases for high availability and horizontal scalability.

- **Caching:**  
  Implement caching solutions (e.g., Redis, Memcached) to store frequent queries and conversation fragments, reducing latency and alleviating pressure on the inference service.

- **Message Queuing:**  
  Use message brokers (e.g., RabbitMQ, Kafka) to manage asynchronous tasks such as logging, notifications, and background processing, ensuring the system remains responsive under heavy load.

### Scalability for 10,000+ Users

- **Horizontal Scaling:**  
  Deploy additional instances of each microservice based on traffic demands. Use auto-scaling features provided by cloud platforms (AWS, GCP, Azure) to dynamically adjust resource allocation.

- **Distributed Infrastructure:**  
  Partition the database and use replication to ensure data consistency and high throughput even when handling many concurrent users.

- **Session Management:**  
  Efficiently manage session data by using in-memory stores and database sharding to provide rapid access to conversation history without performance degradation.

- **Monitoring and Auto-scaling:**  
  Integrate monitoring tools (e.g., Prometheus, Grafana) to observe system performance and trigger auto-scaling policies when specific metrics exceed predetermined thresholds.

---

## Inference Optimization

### Model Optimization

- **Quantization & Distillation:**  
  Reduce model size and inference latency by leveraging techniques like quantization (reducing the precision of model weights) or distillation (training a smaller model to mimic a larger one).

- **Adaptive Inference:**  
  Implement a multi-tiered approach where a lightweight model handles general queries, while more resource-intensive models are engaged for queries requiring higher context sensitivity.

### Request Batching and Caching

- **Batching Requests:**  
  Combine multiple inference requests into a single batch to efficiently utilize GPU/TPU resources and reduce overall response times.
  
- **Response Caching:**  
  Cache frequent or similar requests to minimize redundant computation. This strategy can significantly lower the load on the LLM service during high traffic periods.

### Infrastructure Optimizations

- **GPU/TPU Utilization:**  
  Use cloud-based GPUs or TPUs with autoscaling capabilities to dynamically allocate resources during peak times.
  
- **Model Serving Frameworks:**  
  Leverage frameworks like TensorFlow Serving, TorchServe, or custom inference pipelines that are optimized for production environments to ensure low-latency responses.

---

## Key Technical Decisions

### Choice of LLM Provider

- **Flexibility and Cost:**  
  The system is designed to support integration with various LLM providers (e.g., OpenAI, Anthropic, or open-source models like Llama) based on requirements related to performance, cost, and latency.
  
- **Performance Considerations:**  
  Decision factors include response quality, latency, and throughput, ensuring the selected model meets the needs of high-concurrency environments.

### Architectural Choices

- **Microservices over Monolithic:**  
  The decision to use a microservices architecture allows individual components to be scaled independently, which is critical when dealing with a large number of concurrent users.
  
- **Cloud-Native Infrastructure:**  
  Utilizing cloud services enables rapid scaling, resilience, and ease of management, ensuring that the system can adapt to increasing loads.

### Security and Reliability

- **Data Protection:**  
  Security best practices, such as encrypted communication and secure storage of user data, are integral to protecting sensitive conversation history.
  
- **Resilience:**  
  Implementing failover mechanisms, comprehensive logging, and proactive monitoring ensures that the system remains robust even in the face of unexpected failures.

---

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries listed in `requirements.txt`
- API keys or credentials for the chosen LLM provider

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Seladorr/sarvam_iter1.git
   cd sarvam_iter1
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the chat application with:

```bash
python main.py
```

### Configuration

- **LLM API Credentials:**  
  Set your API keys and other credentials in the configuration file or via environment variables.
  
- **Database Settings:**  
  Configure the database connection in `config.yaml` (or your preferred configuration file).

### Directly building the chatbot using docker desktop

```bash
docker-compose up --build
```

---
