import numpy as np
import random
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Show embeddings stored in the database for a random movie"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())
        if not movies:
            self.stderr.write("❌ No hay películas en la base de datos.")
            return

        # 🎲 Seleccionar una película al azar
        movie = random.choice(movies)

        # 📊 Convertir el campo binario en vector numpy
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)

        # ✅ Mostrar resultados
        self.stdout.write(self.style.SUCCESS(f"🎬 Película seleccionada: {movie.title}"))
        self.stdout.write(f"Dimensión del embedding: {len(embedding_vector)}")
        self.stdout.write(f"Primeros 10 valores: {embedding_vector[:10]}")
