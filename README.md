# **Infosys-Responsible-AI-Toolkit**
The Infosys Responsible AI toolkit provides a set of APIs to integrate safety, privacy, explainability, fairness, and hallucination detection into AI solutions, ensuring trustworthiness and transparency. 

To install any Infosys Responsible AI Toolkit module, open the respective repository and follow the instructions in the README file.

| No. | Module name | Functionalities | Repository names |
| --- | --- | --- | ---- |
| 1 | ModerationLayer APIs (Comprehensive suite of Safety, Privacy, Explainability, Fairness and Hallucination tenets) | To regulate the content of prompts and responses generated by LLMs | [responsible-ai-moderationlayer](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-moderationLayer),<br>[responsible-ai-moderationModel](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-ModerationModel) |
| 2 | Explainability APIs | Get Explainability to LLM responses, Global and local explainability for Regression, Classification and Timeseries Models | [responsible-ai-llm-explain](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-llm-explain),<br>[responsible-ai-explainability](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-explainability),<br>[Model Details](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-model-detail),<br>[Reporting](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-reporting-tool) |
| 3 | Fairness & Bias API | Check Fairness and detect Biases associated with LLM prompts and responses and also for traditional ML models | [responsible-ai-fairness](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-fairness) |
| 4 | Hallucination API | Detect and quantify Hallucination in LLM responses under RAG scenarios | [responsible-ai-hallucination](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-hallucination) |
| 5 | Privacy API | Detect and anonymize or encrypt or hilight PII information in prompts for LLMs or in its responses | [responsible-ai-privacy](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-privacy) |
| 6 | Safety API | Detects and anonymize toxic and profane text associated with LLMs | [responsible-ai-safety](https://github.com/Infosys/Infosys-Responsible-AI-Toolkit/tree/main/responsible-ai-safety) |

These API-based guardrails are being hosted on platforms like Azure OpenAI.

# **Moderating LLM inputs and outputs using Moderation Layer APIs**
This API suite offers a comprehensive set of features for responsible AI. It includes robust moderation capabilities to filter harmful content, advanced prompt engineering techniques to optimize model performance, and powerful explainability tools to understand model reasoning. Additionally, it provides language translation and summarization functionalities using Google or Azure translate, as well as telemetry tracking for monitoring API usage and performance. Refer the 'Moderation API instructions' document for more details on APIs and their functionalities. Here is the quick reference of features under Moderation layer:
* Prompt injection                  
* Jailbreak attempts                
* Toxicity detection               
* Profanity filtering              
* PII identification
* Restricted topic detection
* Factual accuracy
* Bias detection
* Hallucination detection
* Explainability using Chain of thoughts (CoT), Thread of thoughts (ThoT) and Chain of verification (CoV)

If you have more questions or need further insights please feel free to connect with us  Infosysraitoolkit@infosys.com

