# AgapAI: An Attrition Detection Machine Learning Model

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**AgapAI** is an AI-powered dashboard designed to proactively predict employee well-being and attrition risk, serving as an ethical and insightful *kaagapay* (companion) for HR professionals. The name is a portmanteau of "Agap," from the Filipino word *maagap* (meaning proactive or early), and "AI."

This project is an entry for the **BPI DATA Wave 2025**, specifically on **Workplace productivity & Future of Work** track, addressing the challenge of predicting employee well-being and retention ethically in modern work environments.

## Created by:
* **Harold Kim Villapando** | [LinkedIn](https://www.linkedin.com/in/harold-villapando)
* **Elric Kyle Montero** | [LinkedIn](https://www.linkedin.com/in/elric-montero-4a1464309/)
* **Vince Paolo Ramilo** | [LinkedIn](https://www.linkedin.com/in/vince-ramilo-802682380)
* **Gabriel Luigi Virtucio** | [LinkedIn](https://www.linkedin.com/in/gab-virtucio-017138348)

## Table of Contents
1.  [Project Overview](#project-overview)
2.  [The Problem](#the-problem)
3.  [Our Solution](#our-solution)
4.  [Key Features](#key-features)
5.  [Technology Stack](#technology-stack)
6.  [Project Implementation](#project-implementation)
7.  [Data Requirements](#data-requirements)
8. [Challenges, Risks, and Mitigations](#challenges-risks-and-mitigations)
9. [Future Work](#future-work)



## Project Overview

**AgapAI** is an explainable AI dashboard that empowers HR teams in mid-to-large sized firms (Fintech, BPOs) to move from reactive problem-solving to proactive well-being strategy. By analyzing anonymized, consent-driven workplace data, our tool identifies early warning signs of burnout and disengagement, allowing for timely and effective interventions. Our core mission is to enhance employee retention and satisfaction while upholding the highest standards of data privacy and ethics.

---

## The Problem

In today's hybrid work landscape, HR professionals face a significant challenge:
* **Reactive Tools:** Traditional methods like annual surveys or performance reviews are backward-looking and often too late to prevent employee turnover.
* **Data Overload, Insight Deficit:** HR teams have access to data but lack the tools to extract real-time, actionable insights.
* **Ethical Concerns:** Modern AI monitoring tools often create a culture of distrust and raise serious privacy and consent issues.
* **High Costs of Attrition:** Preventable turnover leads to significant financial and institutional knowledge loss.

HR leaders need a solution that is **proactive, trustworthy, and transparent**, flagging attrition risks without compromising employee trust.

---

## Our Solution

We are developing an AI-powered dashboard that predicts employee well-being and attrition risk by analyzing anonymized, consent-driven workplace signals. The model provides both team-level trends for strategic planning and individual risk alerts for targeted support, with all predictions explained in simple, understandable terms.

### Key Features

* **🧠 Explainable AI:** Powered by a machine learning model with SHAP integration to explain the "why" behind every prediction.
* **🔒 Privacy-First by Design:** Built on a non-invasive design and using only anonymized inputs to protect employee privacy and build trust.
* **📊 Interactive Dashboard:** A user-friendly interface for visualizing team-level trends and drilling down into risk factors.
* **💡 Actionable Recommendations:** Provides contextual recommendations to guide HR interventions, helping teams act early and effectively.

---

## Technology Stack

This project prioritizes speed, simplicity, and transparency using a modern, open-source stack.

* **Data Analysis & ML:** NumPy, Pandas, Scikit-learn
* **Explainability:** SHAP (SHapley Additive exPlanations)
* **Dashboard & UI:** HTML & Tailwind CSS
* **Development & Collaboration:** Jupyter Notebook, Google Colab, GitHub

---

## Project Implementation

Our development plan is structured in three key phases for this hackathon:

* **Phase 1: Model Development:** Clean and preprocess a synthetic dataset to train a baseline predictive model using `scikit-learn`.
* **Phase 2: Explainability:** Integrate a SHAP explainability layer on top of the model.

---

## Data Requirements

For the purpose of this hackathon, we will use a static, anonymized, and synthetically generated employee dataset in a `.csv` format. The data is sourced from public repositories like Kaggle.

Key features include, but are not limited to:
* `Employee_Satisfaction_Score`
* `Performance_Score`
* `Work_Hours_Per_Week`
* `Department`
* `Salary`

---

## Challenges, Risks, and Mitigations

We acknowledge several challenges and have proactive strategies to address them.

| Challenge & Risk                       | Mitigation Strategy                                                                                             |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Data Privacy & Consent** | Adopt a **"Privacy by Design"** approach: anonymized views, no PII, and strict adherence to RA 10173 principles.   |
| **Algorithmic Bias** | Conduct model fairness audits (e.g., demographic parity checks) to detect and mitigate biases against protected groups. |
| **Explainability Limitations** | Utilize SHAP's visualization tools and add simple text-based summaries to make insights accessible for non-technical HR users. |
| **Trust and Adoption by Users** | Ground the design in user personas to anticipate and address adoption barriers. Emphasize the tool's role as a support, not a surveillance, mechanism. |
| **Limited Real-World Testing** | Validate the prototype using mock data scenarios and feedback from HR professionals acting as user personas.          |
| **Regulatory Uncertainty** | Include clear disclaimers about the project's non-commercial, proof-of-concept nature and outline a future compliance roadmap. |

---

## Future Work

Following the hackathon, AgapAI has a clear path for growth:
* **Enterprise Integration:** Develop APIs to connect with real-world HRIS (Human Resource Information Systems) for live data analysis.
* **Advanced Modeling:** Explore more complex models (e.g., Gradient Boosting, LSTMs for time-series data) to improve accuracy.
* **Recommendation Engine:** Build a more sophisticated engine that suggests personalized and resource-aware interventions.
* **Compliance Certification:** Work towards formal compliance with the Data Privacy Act (RA 10173) and other relevant regulations for commercial deployment.
