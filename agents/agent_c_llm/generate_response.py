from typing import List, Dict
from dotenv import load_dotenv
import google.generativeai as genai
import os 

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Flash model
model = genai.GenerativeModel("models/gemini-2.0-flash")

def generate_response(chunks: List[Dict], query: str) -> Dict:
    """
    Generates a well-structured answer using provided chunks and user query.
    
    Args:
        chunks (List[Dict]): List of document chunks. Each should contain:
            - content (str)
            - source_file (str)
            - page (int)
        query (str): The user question.

    Returns:
        Dict: A structured answer with reasoning and references.
    """
    context = "\n\n".join(
        f"[{chunk['source_file']} - Page {chunk['page']}]: {chunk['content']}" for chunk in chunks
    )

    prompt = f"""You are an expert assistant. Answer the following question using only the provided context.
    Context:
    {context}

    Question:
    {query}

    Answer the question clearly and concisely. Cite sources using the format: [filename - Page X].
    """

    try:
        response = model.generate_content(prompt)
        return {
            "query": query,
            "answer": response.text.strip()
        }
    except Exception as e:
        return {
            "query": query,
            "answer": f"An error occurred while generating the response: {str(e)}"
        }

if __name__ == "__main__":
    sample_result_from_retriever = [{'content': 'architecture, we\nexperiment with the recently introduced Vision Transformer\n(ViT) (Dosovitskiy et al., 2020). We closely follow their\nimplementation with only the minor modiﬁcation of adding\nan additional layer normalization to the combined patch\nand position embeddings before the transformer and use a\nslightly different initialization scheme.\nThe text encoder is a Transformer (Vaswani et al., 201', 'source_file': 'CLIP.pdf', 'page': 5}, {'content': 'pace. See Appendix D.7 for\ndetails.To begin to understand how the Vision Transformer processes im-\nage data, we analyze its internal representations. The ﬁrst layer of\nthe Vision Transformer linearly projects the ﬂattened patches into a\nlower-dimensional space (Eq. 1). Figure 7 (left) shows the top prin-\ncipal components of the the learned embedding ﬁlters. The com-\nponents resemble plausible basi', 'source_file': 'VisionTransformer.pdf', 'page': 8}, {'content': 'l contribution,yequal advising\nGoogle Research, Brain Team\nfadosovitskiy, neilhoulsby g@google.com\nABSTRACT\nWhile the Transformer architecture has become the de-facto standard for natural\nlanguage processing tasks, its applications to computer vision remain limited. In\nvision, attention is either applied in conjunction with convolutional networks, or\nused to replace certain components of convoluti', 'source_file': 'VisionTransformer.pdf', 'page': 1}, {'content': 'ncoder as used in NLP. This simple,\nyet scalable, strategy works surprisingly well when coupled with pre-training on large datasets.\nThus, Vision Transformer matches or exceeds the state of the art on many image classiﬁcation\ndatasets, whilst being relatively cheap to pre-train.\nWhile these initial results are encouraging, many challenges remain. One is to apply ViT to other\ncomputer vision tasks,', 'source_file': 'VisionTransformer.pdf', 'page': 9}, {'content': 'nal\nimage. Note that this resolution adjustment and patch extraction are the only points at which an\ninductive bias about the 2D structure of the images is manually injected into the Vision Transformer.\n4 E XPERIMENTS\nWe evaluate the representation learning capabilities of ResNet, Vision Transformer (ViT), and the\nhybrid. To understand the data requirements of each model, we pre-train on datasets ', 'source_file': 'VisionTransformer.pdf', 'page': 4}]
    sample_query_used = "What is a vision transformer?"
    ans = generate_response(sample_result_from_retriever, sample_query_used)
    print(ans)