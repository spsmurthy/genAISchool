from ingestion.pdf_loader import load_and_chunk_pdf
from ingestion.embedder import embed_chunks
from retrieval.rag_pipeline import get_answer
from narration.script_generator import enhance_topic
from narration.tts_engine import generate_audio
from video.video_shell import generate_video_stub

if __name__ == "__main__":
    chunks = load_and_chunk_pdf("sample.pdf")
    embed_chunks(chunks)

    user_question = "Explain photosynthesis like a story."
    answer = get_answer(user_question)

    script = enhance_topic(answer)
    generate_audio(script, filename="audio_output.mp3")

    generate_video_stub(script, audio_path="audio_output.mp3")