# Fine-Tuning Tiny Llama using Llama Factory To Mimic Professor's Writing Style
## Overview
This project aims to fine-tune the Tiny Llama model using the Llama Factory to mimic my professor's writing style. The process involves several phases, including data collection, preprocessing, preparation, model fine-tuning, and evaluation. The final goal is to create a model that can generate text in the style of my professor's academic writings.

## Phases of the Project
### Phase 1: Data Collection
The first step in this project was to collect data by scraping my professor's Google Scholar page. The objective was to gather a comprehensive set of research articles published by the professor.

- **Tool Used:** Selenium
- **Details:** Selenium was used to automate the process of accessing the Google Scholar page and downloading the available PDFs of the research articles.
### Phase 2: Data Preprocessing
After collecting the PDFs, the next step was to preprocess these documents to ensure they were in a usable format for training the model.

- **Purpose:** Normalize the content while preserving the writing style.
- **Tools Used:** pyMuPDF
### Steps:
- Remove page headers, footers, images, and tables along with their captions.
- Convert the remaining content into paragraph format, as individual words and phrases are insufficient for capturing writing style.
### Phase 3: Data Preparation
The preprocessed data needed to be formatted according to the requirements of the Llama Factory model training process.

- **Initial Tools Tried:** spaCy, TF-IDF, BERT
- **Tool That Worked:** OpenAI API
### Process:
- Use the OpenAI API to generate the required data format.
- Ensure that the data is structured correctly for input into the Llama Factory model.
### Phase 4: Model Fine-Tuning
With the data prepared, the next phase involved fine-tuning the Tiny Llama model.

- **Environment:** Google Colab
- **Tools Used:** Llama Factory
### Steps:
- Set up the Google Colab notebook and import necessary libraries.
- Load the Llama Factory UI and integrate the dataset.
- Define the prompt format and other configurations required by Llama Factory.
- Run the fine-tuning process to train the Tiny Llama model on the professor's writing style.
### Phase 5: Model Evaluation
The final phase focused on evaluating the performance of the fine-tuned model to ensure it accurately mimics the professor's writing style.

### Process:
- Generate sample texts using the fine-tuned model.
- Compare the generated texts with the original writings to assess similarity in style and content.
- Make any necessary adjustments and re-train if needed.
## Getting Started
### Prerequisites
- Python 3.x
- Selenium
- pyMuPDF
- OpenAI API
### Installation
- Clone the repository
```bash
git clone https://github.com/yourusername/finetuning-tiny-llama.git
```
- Install the necessary Python packages
```bash
pip install selenium pymupdf openai
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or suggestions, please contact me at muhammadmuneeburrehman.vercel.app
