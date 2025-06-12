import torchaudio
from audiocraft.models import AudioGen
from audiocraft.data.audio import audio_write

model = AudioGen.get_pretrained('facebook/audiogen-medium')
model.set_generation_params(duration=5)

def generate_music(description: str):
    wav = model.generate(description)

    for idx, one_wav in enumerate(wav):
        audio_write('sample', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)