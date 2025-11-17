# SDUs Daisy: A Benchmark for Danish Culture 
<p align="center">
  <img src="docs/daisy_logo.png" alt="Description" width="250"/>
</p>


**SDU DAISY** is the first version of a dataset designed to **evaluate large language models’ understanding of Danish culture**, as defined by the official **Danish Culture Canon (Kulturkanon, 2006)**, defined by 746 closed question-answer pairs.  

The Canon highlights 108 works across literature, music, visual arts, architecture, design, film, and performing arts. These works form a curated benchmark of what is often considered Denmark’s cultural heritage. By using them as anchors, this dataset enables systematic investigation of how well LLMs can reason about, contextualize, and generate insights into Danish culture.  

---

## Why this dataset?  

- **Cultural Relevance Test** – The Canon provides a well-defined cultural benchmark for evaluation.  
- **Knowledge Probing** – Randomized prompts (Danish "*stikprøvekontrol*) test both relevant and less relevant associations with Canon works.
- **Human Validation** – Every generated question/response pair is annotated for validation and relevance, even though we both want to main- and non-mainstream knowledge. 

---

## Methodology  

1. **Sampling (*Stikprøvekontrol*)**  
   For each Canon title, random questions are generated — ranging from directly relevant inquiries (e.g., about historical context) to more peripheral or unexpected ones.  

2. **Response Collection**  
   LLMs provide answers to these questions, creating a structured dataset of outputs.  

3. **Human Evaluation**  
   - **Relevance** (on-topic vs. off-topic)  
   - **Accuracy** (correct vs. incorrect)  
   - **Cultural Insight** (does it capture nuance/meaning? - also including small or even niece facts)  

---

## Applications 

- Benchmarking **LLM performance on Danish culturally sub-domains**  
- Supporting **digital humanities research** on how AI engages with cultural canons  
- Encouraging critical reflection on the **boundaries of cultural knowledge** encoded in AI systems  

---

# SDU Daisy Evaluations 
<table style="width:100%; border-collapse:collapse; font-family:sans-serif; color: white; background:rgba(9, 21, 54, 1) ; border:1px solid rgba(119, 158, 203, 1);">
  <tr style="background:rgba(9, 21, 54, 1); color:white">
    <th style="padding:10px; text-align:left; color:white;">Model</th>
    <th style="padding:10px;">F1 Score</th>
    <th style="padding:10px;">Bleu</th>
    <th style="padding:10px;">Dataset Version</th>
    <th style="padding:10px;">Prompt Template Version</th>
  </tr>

  <tr style="background:#161b22;">
    <td style="padding:10px; text-align:left;">openai/gpt-oss-20b</td>
    <td style="padding:10px; text-align:center;">-</td>
    <td style="padding:10px; text-align:center;">-</td>
    <td style="padding:10px; text-align:center;">1.0</td>
    <td style="padding:10px; text-align:center;">1.0</td>
  </tr>

  <tr style="background:#0f131a;">
    <td style="padding:10px; text-align:left;">openai/gpt-oss-120b</td>
    <td style="padding:10px; text-align:center;">-</td>
    <td style="padding:10px; text-align:center;">-</td>
    <td style="padding:10px; text-align:center;">1.0</td>
    <td style="padding:10px; text-align:center;">1.0</td>
  </tr>

  <tr style="background:#161b22;">
    <td style="padding:10px; text-align:left;">google/gemma-3-27b-it</td>
    <td style="padding:10px; text-align:center;">-</td>
    <td style="padding:10px; text-align:center;">-</td>
    <td style="padding:10px; text-align:center;">1.0</td>
    <td style="padding:10px; text-align:center;">1.0</td>
  </tr>
</table>
