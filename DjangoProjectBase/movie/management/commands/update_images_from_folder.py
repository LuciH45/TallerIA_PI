import os
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Assign images from local folder (media/movie/images/) to movies in the database"

    def handle(self, *args, **kwargs):
        # 📂 Carpeta donde ya están guardadas las imágenes
        images_folder = os.path.join("media", "movie", "images")

        if not os.path.exists(images_folder):
            self.stderr.write(f"Folder not found: {images_folder}")
            return

        updated_count = 0
        not_found_count = 0

        # 🔎 Recorremos todas las películas en la base de datos
        for movie in Movie.objects.all():
            # Nombre esperado de la imagen
            expected_filename = f"m_{movie.title}.png"
            expected_path = os.path.join(images_folder, expected_filename)

            if os.path.exists(expected_path):
                # Guardamos ruta relativa en el campo de la película
                movie.image = os.path.join("movie", "images", expected_filename)
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"✅ Updated image for: {movie.title}"))
            else:
                not_found_count += 1
                self.stderr.write(f"⚠️ Image not found for: {movie.title} (expected {expected_filename})")

        self.stdout.write(self.style.SUCCESS(
            f"Finished updating {updated_count} movies. {not_found_count} images not found."
        ))
