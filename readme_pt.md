
Gerador de Áudio Binaural com Ruído Rosa (Python)
=================================================

Este projeto gera um áudio estéreo com batimento binaural de 40 Hz (440 Hz no ouvido esquerdo e 480 Hz no direito),
misturado com ruído rosa de fundo, com duração de 10 minutos.

Ideal para concentração, foco e suporte a práticas como brainwave entrainment.

Requisitos
----------

- Python 3.10 ou superior
- Pip
- FFmpeg instalado e configurado
- Bibliotecas Python: pydub, numpy, scipy

Instalação
----------

1. Instalar dependências Python:

    pip install pydub numpy scipy

2. Baixar e configurar o FFmpeg:

   - Baixe o FFmpeg por este link:
     https://objects.githubusercontent.com/github-production-release-asset-2e65be/292087234/049b6494-41db-4b3c-b705-d0917d549bcc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250602%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250602T190658Z&X-Amz-Expires=300&X-Amz-Signature=68a663be42f93dd5db9615a99b180834ac35f0486947d6facf4f783b0e6ee054&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dffmpeg-master-latest-win64-gpl-shared.zip&response-content-type=application%2Foctet-stream

   - Extraia o arquivo em um diretório como: C:\ffmpeg\

   - Verifique se existe o arquivo: C:\ffmpeg\bin\ffmpeg.exe

   - Adicione o caminho ao PATH do sistema:
     1. Painel de Controle → Sistema → Configurações Avançadas do Sistema
     2. Variáveis de Ambiente → selecione "Path" → Editar
     3. Clique em "Novo" e adicione: C:\ffmpeg\bin
     4. Reinicie o terminal

   - Teste com: ffmpeg -version

Execução
--------

- Salve o script Python no mesmo diretório deste README
- Execute com:

    python binaural_40hz_pink_noise.py

- O áudio será salvo em: C:\tmp\binaural_40hz_10min_pink_noise.wav

Problemas Comuns
----------------

- Erro: "Couldn't find ffmpeg or avconv"
  Solução: adicione esta linha ao início do script:

    from pydub import AudioSegment
    AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"

Licença
-------

Uso livre para fins pessoais, acadêmicos e terapêuticos.

