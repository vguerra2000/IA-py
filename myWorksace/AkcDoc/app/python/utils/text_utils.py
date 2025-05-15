import re
from typing import List

class TextProcessor:
    """
    Clase para limpieza y fragmentación de texto.
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Normaliza el texto:
        - Convierte saltos de línea múltiples en uno solo.
        - Elimina caracteres no imprimibles.
        - Reemplaza espacios múltiples por un único espacio.
        - Recorta espacios al inicio y final.

        Args:
            text (str): Texto original.
        Returns:
            str: Texto limpio.
        """
        text = re.sub(r"[\r\t\v]+", " ", text)
        text = re.sub(r"\n+", "\n", text)
        text = re.sub(r"[ ]{2,}", " ", text)
        text = "\n".join(line.strip() for line in text.split("\n"))
        return text.strip()

    @staticmethod
    def fragment(text: str, max_chars: int = 1000, overlap: int = 200) -> List[str]:
        """
        Divide el texto en fragmentos de longitud óptima para análisis.

        Args:
            text (str): Texto limpio.
            max_chars (int): Tamaño máximo de cada fragmento.
            overlap (int): Solapamiento entre fragmentos.

        Returns:
            List[str]: Lista de fragmentos.
        """
        fragments = []
        start = 0
        text_length = len(text)
        while start < text_length:
            end = start + max_chars
            fragment = text[start:end]
            fragments.append(fragment)
            start = end - overlap
            if start < 0:
                start = 0
        return fragments
