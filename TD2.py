{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "TD2.py",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AxelBattut/TD02BitcoinGuittonBattut/blob/main/TD2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JfRfDBatkNE1",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 190
        },
        "outputId": "cf65189f-9e08-4cda-cad4-398ce184688f"
      },
      "source": [
        "#Créer un entier aléatoire pouvant servir de seed à un wallet de façon sécurisée\n",
        "import secrets\n",
        "sec=secrets.randbits(128)\n",
        "print('nombre sécurisé de 128 bits généré aléatoirement :',sec,'\\n') #on obtient ici notre nombre de taille  bits généré aléatoirement \n",
        "\n",
        "secbin=bin(sec) #fonction bin pour convertir un décimal en binaire \n",
        "secbinbon = secbin[2:len(secbin)] # secbinbon est notre chiffre binaire sans le 0b\n",
        "print('le même nombre généré en binaire :',secbinbon,'\\n')\n",
        "\n",
        "\n",
        "\n",
        "b= secbinbon\n",
        "#b= '1110000010110010100100011101001100110001110111111011011001010110111111001101010110111011111011000101001001001100011011111011000000'\n",
        "bcomp='0' #cas 131 par defaut (le cas 132 n'existe pas)\n",
        "if (132-len(b) == 2): #cas 130\n",
        "  bcomp = '00'\n",
        "if (132-len(b) == 3): #etc..\n",
        "  bcomp = '000'\n",
        "if (132-len(b) == 4): \n",
        "  bcomp = '0000'\n",
        "if (132-len(b) == 5): \n",
        "  bcomp = '00000'\n",
        "if (132-len(b) == 6): \n",
        "  bcomp = '000000'\n",
        "if (132-len(b) == 7): \n",
        "  bcomp = '0000000'\n",
        "if (132-len(b) == 8): \n",
        "  bcomp = '00000000'\n",
        "if (132-len(b) == 9): \n",
        "  bcomp = '000000000'\n",
        "if (132-len(b) == 10): \n",
        "  bcomp = '0000000000'\n",
        "if (132-len(b) == 11): \n",
        "  bcomp = '00000000000'\n",
        "if (132-len(b) == 12): \n",
        "  bcomp = '000000000000'\n",
        "b = ''.join((b,bcomp))\n",
        "\n",
        "print('le même nombre généré en binaire sur 132bits', b,'\\n')\n",
        "\n",
        "with open(\"englishlist.txt\",\"r\") as f:\n",
        "  wordlist= [w.strip() for w in f.readlines()] \n",
        "  seed = []\n",
        "  for i in range(len(b)//11): #12 itérations\n",
        "    indx = int(b[11*i:11*(i+1)],2) #l'index correspond à la chaine de 11 caractères \n",
        "    seed.append(wordlist[indx]) #on ajoute le mot correspondant à l'index à chaque itération\n",
        "  print('la seed de 12 mots générée :', seed)\n",
        " \n",
        "\n",
        "\n"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "nombre sécurisé de 128 bits généré aléatoirement : 296682138843614070096909021127507245997 \n",
            "\n",
            "le même nombre généré en binaire : 11011111001100101110011011001001110001101111101100010111100110110110100100110010000000110100101001111001101001001111101110101101 \n",
            "\n",
            "le même nombre généré en binaire sur 132bits 110111110011001011100110110010011100011011111011000101111001101101101001001100100000001101001010011110011010010011111011101011010000 \n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-8fdef545-fcb2-4897-8489-f814ba289725\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-8fdef545-fcb2-4897-8489-f814ba289725\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving englishlist.txt to englishlist.txt\n",
            "la seed de 12 mots générée : ['tennis', 'now', 'raven', 'mistake', 'ramp', 'soap', 'pill', 'document', 'engine', 'snake', 'discover', 'foam']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ixm9IIAJChpx",
        "outputId": "22c7d112-1d98-4806-d0f4-2121fd23b37e"
      },
      "source": [
        "\n",
        "import urllib.request as urllib\n",
        "import json\n",
        "\n",
        "# Load the bitcoin BIP39 english word dictionary, total 2048 words\n",
        "wordListUrl = \"https://raw.githubusercontent.com/bitcoinjs/bip39/master/src/wordlists/english.json\"\n",
        "wordlist = list(json.load(urllib.urlopen(wordListUrl)))\n",
        "\n",
        "# Creates 2 dictionarys\n",
        "def createDic():\n",
        "    alphadic = {}  # Maps word as key to int as value\n",
        "    ralphadic = {}  # Reverses alphadic\n",
        "\n",
        "    linenumber = 0\n",
        "    for line in wordlist:\n",
        "        alphadic[line] = linenumber\n",
        "        ralphadic[linenumber] = line\n",
        "        linenumber += 1\n",
        "\n",
        "    return alphadic, ralphadic\n",
        "# mnemonic decoding algorithm, decode a mnemonic string back to the orinal hex number\n",
        "\n",
        "def decode(s):\n",
        "    alphadic, _ = createDic()\n",
        "    l=[]\n",
        "\n",
        "    for word in s.split():\n",
        "        w = bin(alphadic[word])[2:]\n",
        "        a = \"0\" * (11 - len(w) ) + w\n",
        "        l.append(a)\n",
        "    r = \"\".join(l)\n",
        "    out = \"\"\n",
        "    for i in range(0, len(r), 4):\n",
        "        out += hex(int(r[i: i + 4], 2))[2:]\n",
        "    return out\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  # TODO: remove the trailing extra 0s\n",
        "  print('Merci de rentrer une seed memnonique de 12 mots (english) :\\n')\n",
        "seed = str(input())\n",
        "print('\\n')\n",
        "print('L entropy est :' ,\n",
        "      decode(seed))\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Merci de rentrer une seed memnonique de 12 mots (english) :\n",
            "\n",
            "abandon world act adult attract hello home run three trade twin wheel\n",
            "\n",
            "\n",
            "L entropy est : 001fb40981e0ecd59b45eae11cd7adfd0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_OB89xBAcAAn",
        "outputId": "925cfc45-a8ef-491b-8e1c-9237fc83de62"
      },
      "source": [
        "!pip install ecdsa\n",
        "\n",
        "import binascii\n",
        "import hmac\n",
        "import hashlib\n",
        "import ecdsa\n",
        "import struct\n",
        "from ecdsa.curves import SECP256k1\n",
        "from ecdsa.ecdsa import int_to_string, string_to_int\n",
        "\n",
        "class B58():\n",
        "\n",
        "    def b58encode(v):\n",
        "        alphabet = \"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz\"\n",
        "        # print(binascii.hexlify(v))\n",
        "        p, acc = 1, 0\n",
        "        for c in reversed(v):\n",
        "            # print(\"c: {}\".format(c))\n",
        "            acc += p * c\n",
        "            # print(\"acc: {}\".format(acc))\n",
        "            p = p << 8\n",
        "            # print(\"p: {}\".format(p))\n",
        "\n",
        "        string = \"\"\n",
        "        while acc:\n",
        "            acc, idx = divmod(acc, 58)\n",
        "            string = alphabet[idx : idx + 1] + string\n",
        "        return string\n",
        "\n",
        "#chain m\n",
        "seed = binascii.unhexlify(\"000102030405060708090a0b0c0d0e0f\")  # generate a seed byte sequence S of a chosen length (beween 128 and 512 bits)\n",
        "I = hmac.new(b\"Bitcoin seed\", seed, hashlib.sha512).digest() #calculate HMAC-SHA512 of seed Key= \"Bitcoin seed\" Data = seed\n",
        "Il, Ir = I[:32], I[32:]  # Divide HMAC into \"Left\" and \"Right\" section of 32 bytes each :) \n",
        "\n",
        "# Serialization format can be found at: https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#Serialization_format\n",
        "secret = Il # left section of HMAC: source to generate keypair\n",
        "chain = Ir # right section of HMAC: chain code\n",
        "xprv = binascii.unhexlify(\"0488ade4\") # Version string for mainnet extended private keys\n",
        "xpub = binascii.unhexlify(\"0488b21e\") # Version string for mainnet extended public keys\n",
        "depth = b\"\\x00\" # Child depth; parent increments its own by one when assigning this\n",
        "fpr = b'\\0\\0\\0\\0' # Parent fingerprint,\n",
        "index = 0 # Child index\n",
        "child = struct.pack('>L', index)  # >L -> big endian -> the way of storing values starting from most significant value in sequence\n",
        "\n",
        "k_priv = ecdsa.SigningKey.from_string(secret, curve=SECP256k1)\n",
        "K_priv = k_priv.get_verifying_key()\n",
        "\n",
        "data_priv = b'\\x00' + (k_priv.to_string())  # ser256(p): serializes integer p as a 32-byte sequence\n",
        "\n",
        "# serialization the coordinate pair P = (x,y) as a byte sequence using SEC1's compressed form\n",
        "if K_priv.pubkey.point.y() & 1:\n",
        "    data_pub= b'\\3'+int_to_string(K_priv.pubkey.point.x())\n",
        "else:\n",
        "    data_pub = b'\\2'+int_to_string(K_priv.pubkey.point.x())\n",
        "\n",
        "raw_priv = xprv + depth + fpr + child + chain + data_priv\n",
        "raw_pub = xpub + depth + fpr + child + chain + data_pub\n",
        "\n",
        "# Double hash using SHA256\n",
        "hashed_xprv = hashlib.sha256(raw_priv).digest()\n",
        "hashed_xprv = hashlib.sha256(hashed_xprv).digest()\n",
        "hashed_xpub = hashlib.sha256(raw_pub).digest()\n",
        "hashed_xpub = hashlib.sha256(hashed_xpub).digest()\n",
        "\n",
        "# Append 4 bytes of checksum\n",
        "raw_priv += hashed_xprv[:4]\n",
        "raw_pub += hashed_xpub[:4]\n",
        "\n",
        "# Affichage\n",
        "print('\\n')\n",
        "print('master private key :',B58.b58encode(raw_priv),'\\n')\n",
        "print('master public key :' ,B58.b58encode(raw_pub),'\\n')\n",
        "print('chain code (hex):' ,chain.hex(),'\\n')\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting ecdsa\n",
            "  Downloading ecdsa-0.17.0-py2.py3-none-any.whl (119 kB)\n",
            "\u001b[?25l\r\u001b[K     |██▊                             | 10 kB 23.7 MB/s eta 0:00:01\r\u001b[K     |█████▌                          | 20 kB 9.5 MB/s eta 0:00:01\r\u001b[K     |████████▎                       | 30 kB 8.0 MB/s eta 0:00:01\r\u001b[K     |███████████                     | 40 kB 7.5 MB/s eta 0:00:01\r\u001b[K     |█████████████▊                  | 51 kB 4.0 MB/s eta 0:00:01\r\u001b[K     |████████████████▌               | 61 kB 4.3 MB/s eta 0:00:01\r\u001b[K     |███████████████████▏            | 71 kB 4.4 MB/s eta 0:00:01\r\u001b[K     |██████████████████████          | 81 kB 4.9 MB/s eta 0:00:01\r\u001b[K     |████████████████████████▊       | 92 kB 3.7 MB/s eta 0:00:01\r\u001b[K     |███████████████████████████▌    | 102 kB 4.0 MB/s eta 0:00:01\r\u001b[K     |██████████████████████████████▏ | 112 kB 4.0 MB/s eta 0:00:01\r\u001b[K     |████████████████████████████████| 119 kB 4.0 MB/s \n",
            "\u001b[?25hRequirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.7/dist-packages (from ecdsa) (1.15.0)\n",
            "Installing collected packages: ecdsa\n",
            "Successfully installed ecdsa-0.17.0\n",
            "\n",
            "\n",
            "master private key : xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi \n",
            "\n",
            "master public key : xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8 \n",
            "\n",
            "chain code (hex): 873dff81c02f525623fd1fe5167eac3a55a049de3d314bb42ee227ffed37d508 \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "cellView": "code",
        "id": "VGsQgvl5L0Fr",
        "outputId": "daea7fb0-9d82-42b6-a822-810cfa221642"
      },
      "source": [
        "#@title Titre par défaut\n",
        "!pip install Mnemonic\n",
        "!pip install bip32utils\n",
        "from mnemonic import Mnemonic\n",
        "import bip32utils\n",
        "\n",
        "mnemon = Mnemonic('english')\n",
        "#words = mnemon.generate(256)\n",
        "#print(words)\n",
        "#mnemon.check(words)\n",
        "#seed = mnemon.to_seed(words)\n",
        "seed = mnemon.to_seed(b'abandon amount liar amount expire adjust cage candy arch gather drum buyer')\n",
        "print(f'BIP39 Seed: {seed.hex()}\\n')\n",
        "\n",
        "root_key = bip32utils.BIP32Key.fromEntropy(seed)\n",
        "\n",
        "child_key = root_key.ChildKey(0).ChildKey(0)\n",
        "child_address = child_key.Address()\n",
        "child_public_hex = child_key.PublicKey().hex()\n",
        "child_private_wif = child_key.WalletImportFormat()\n",
        "\n",
        "child_key2 = root_key.ChildKey(0).ChildKey(2)\n",
        "child_address2 = child_key2.Address()\n",
        "child_public2_hex = child_key2.PublicKey().hex()\n",
        "child_private2_wif = child_key2.WalletImportFormat()\n",
        "\n",
        "print('Clef enfant:')\n",
        "print(f'\\tAddress: {child_address}')\n",
        "print(f'\\tPublic (hex): {child_public_hex}')\n",
        "print(f'\\tPrivate (wif) : {child_private_wif}\\n')\n",
        "\n",
        "print('Clef enfant à l index 2:')\n",
        "print(f'\\tAddress: {child_address2}')\n",
        "print(f'\\tPublic (hex): {child_public2_hex}')\n",
        "print(f'\\tPrivate (wif) : {child_private2_wif}')\n",
        "\n"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting Mnemonic\n",
            "  Downloading mnemonic-0.20-py3-none-any.whl (62 kB)\n",
            "\u001b[K     |████████████████████████████████| 62 kB 482 kB/s \n",
            "\u001b[?25hInstalling collected packages: Mnemonic\n",
            "Successfully installed Mnemonic-0.20\n",
            "Collecting bip32utils\n",
            "  Downloading bip32utils-0.3.post4-py3-none-any.whl (9.9 kB)\n",
            "Requirement already satisfied: ecdsa in /usr/local/lib/python3.7/dist-packages (from bip32utils) (0.17.0)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.7/dist-packages (from ecdsa->bip32utils) (1.15.0)\n",
            "Installing collected packages: bip32utils\n",
            "Successfully installed bip32utils-0.3.post4\n",
            "BIP39 Seed: 3779b041fab425e9c0fd55846b2a03e9a388fb12784067bd8ebdb464c2574a05bcc7a8eb54d7b2a2c8420ff60f630722ea5132d28605dbc996c8ca7d7a8311c0\n",
            "\n",
            "Clef enfant:\n",
            "\tAddress: 125wydPD1UXCex7LCFyyDqVuNUPa19zcCX\n",
            "\tPublic (hex): 027e093fabac4d5e624b56a49c892a0e8a1c49032ec2590912838dfb8007b0d2e3\n",
            "\tPrivate (wif) : L2qLJz7yorJvmerSaZVrszXaNGeiXAK6icAX49DmtjTjWaFWjhFG\n",
            "\n",
            "Clef enfant à l index 2:\n",
            "\tAddress: 1HsCVfXUhKvX2Zw9e14xgu1eQ5MH7DCkWf\n",
            "\tPublic (hex): 0345e975d9fe67e5da319bc1f3f7dd79a9b6a41777a998ee72a8c012e496bd4289\n",
            "\tPrivate (wif) : KzQqss4wxB3298LumY1F3kPk2aw2ywJNKC9UJXqRvNWDDRBBJZpC\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aE1_NdGjO6la"
      },
      "source": [
        "Si un pirate met la main sur une clé privée enfant et la clé xpub du compte, le pirate peut recalculer la clé xprv du compte et ainsi avoir accès à chaque clé privée et publique descendant du niveau du compte."
      ]
    }
  ]
}