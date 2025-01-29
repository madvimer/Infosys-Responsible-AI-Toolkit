# **Infosys-Responsible-AI-Toolkit**
The Infosys Responsible AI toolkit provides a set of APIs to integrate safety,security, privacy, explainability, fairness, and hallucination detection into AI solutions, ensuring trustworthiness and transparency. 

### Repositories and Installation Instructions
The following table lists the modules of the Infosys Responsible AI Toolkit.  Installation instructions for each module can be found in the corresponding README file within the module's directory.

| # | Module | Functionalities | Repository name(s) |
| --- | --- | --- | ---- |
| 1 | ModerationLayer APIs <br>(Comprehensive suite of Safety, Privacy, Explainability, Fairness and Hallucination tenets) | To regulate the content of prompts and responses generated by LLMs | [responsible-ai-moderationlayer](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-moderationLayer),<br>[responsible-ai-moderationModel](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-ModerationModel) |
| 2 | Explainability APIs** | Get Explainability to LLM responses, <br>Global and local explainability for Regression, Classification and Timeseries Models | [responsible-ai-llm-explain](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-llm-explain),<br>[responsible-ai-explainability](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-explainability),<br>[Model Details](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-model-detail),<br>[Reporting](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-reporting-tool) |
| 3 | Fairness & Bias API | Check Fairness and detect Biases associated with LLM prompts and responses and also for traditional ML models | [responsible-ai-fairness](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-fairness) |
| 4 | Hallucination API | Detect and quantify Hallucination in LLM responses under RAG scenarios | [responsible-ai-hallucination](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-hallucination) |
| 5 | Privacy API | Detect and anonymize or encrypt or hilight PII information in prompts for LLMs or in its responses | [responsible-ai-privacy](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-privacy) |
| 6 | Safety API | Detects and anonymize toxic and profane text associated with LLMs | [responsible-ai-safety](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-safety) |
| 7 | Security API | For different types of security attacks and defenses on tabular and image data, prompt injection and jailbreak checks | [responsible-ai-security](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/Responsible-AI-Security-API) |

** Endpoints for explainability are located in both the explainability and moderation layer repositories. Refer to the README files in these repositories for more details on specific features.

### Modules for the Responsible AI Toolkit Interface
The Responsible AI toolkit provides a user-friendly interface for seamless experimentation and alignment with various Responsible AI principles. The following APIs are required to activate and utilize the toolkit's UI. To access the toolkit through the interface, refer to the README files associated with the listed repositories.
| # | Module | Functionalities | Repository name(s) |
| --- | --- | --- | ---- |
| 1 | MFE |  An Angular micro frontend app serves as a user interface where users can easily interact with and consume various backend endpoints through independently developed, modular components. | [responsible-ai-mfe](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/Infosys-Responsible-AI-Toolkit-v2.1.0/responsible-ai-mfe) |
| 2 | SHELL |  A shell application in a micro frontend architecture acts as the central hub, orchestrating and loading independent frontend modules. It provides a unified user interface where users can interact with different micro frontends, consume backend endpoints.| [responsible-ai-shell](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/Infosys-Responsible-AI-Toolkit-v2.1.0/responsible-ai-shell) |
| 3 | Backend |  A Python backend module focused on registration and authentication handles user account management, including user registration, login, password validation, and session management.| [responsible-ai-backend](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/Infosys-Responsible-AI-Toolkit-v2.1.0/responsible-ai-backend) |
| 4 | Telemetry | A python backend module defining the various tenets structure for ingestion of the API's data into Elasticsearch indexes. It provided customizable input validation and insertion of data coming from tenets into elasticsearch, which can be further displayed using kibana.| [responsible-ai-telemetry](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/Infosys-Responsible-AI-Toolkit-v2.1.0/responsible-ai-telemetry) |
| 5 | File Storage | Python module that provides versatile APIs for seamless integration across multiple microservices, enabling efficient file management with Azure Blob Storage. It supports key operations such as file upload, retrieval, and updates, offering a robust solution for handling files in Azure Blob Storage.| [responsible-ai-file-storage](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/Infosys-Responsible-AI-Toolkit-v2.1.0/responsible-ai-file-storage) |
| 6 | Benchmarking | Displays stats related to benchmarking large language models (LLMs) across various categories such as fairness, privacy, truthfulness and ethics. It helps evaluate and compare LLM performance in these critical areas.| [responsible-ai-llm-benchmarking](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/Infosys-Responsible-AI-Toolkit-v2.1.0/responsible-ai-llm-benchmarking)|

Please refer [Features and Endpoints](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/blob/main/Reference%20Guide%20-%20Features%20and%20Endpoints.pdf) document for more details.

Note: These API-based guardrails are optimized for Azure OpenAI. Users employing alternative LLMs should make the necessary client configuration adjustments. For Azure OpenAI api subscription, follow instructions provided in the [Microsoft Azure website](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=ai-services&azure-portal=true).

### Snapshot of the Features
#### Generative AI Models
| Safety, Security & Privacy | Model Transparency  | Text Quality | Linguistic Quality |
|:--- |:--- |:----  |:---- |
|Prompt Injection Score <br>Jailbreak Score <br>Privacy check <br>Profanity check <br>Restricted Topic check <br>Toxicity check <br>Refusal check | Sentiment check <br>Fairness & Bias check <br>Hallucination Score <br>Explainability using<br>-Thread of Thoughts (ToT) <br>-Chain of Thoughts (CoT) <br>-Graph of Thoughts (GoT) <br>Token Importance |Invisible Text, Gibberish Checks <br>Ban Code Check <br>Completeness check <br>Conciseness check <br>Text Quality check<br>Text Relevance check <br>Uncertainty Score <br>Coherence Score |Language Critique Coherence check <br>Language Critique Fluency check <br>Language Critique Grammar check <br>Language Critique Politeness check  |

#### Machine Learning Models
| Security | Fairness | Explainability |
|:--- |:--- |:----  |
|Simulate Adverserial Attacks<br>Recommend Defense Mechanism |Bias Detection Methods<br>-Statistical Parity Difference<br>-Disparate Imapct Ratio<br>-Four Fifth's Rule<br>-Cohen's D<br>Mitigation Methods:<br>-Equalized Odds<br>-Re-weighing |Global Explainability using LIME<br>Local Explainability using SHAP |

If you have more questions or need further insights please feel free to connect with us  Infosysraitoolkit@infosys.com

