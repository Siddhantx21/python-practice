{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoYYEkA5+SnRxqw4j7BR0L",
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
        "<a href=\"https://colab.research.google.com/github/Siddhantx21/python-practice/blob/main/day%204_case%20cond.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ulBRpdtgL7AJ",
        "outputId": "4eb48dac-cd08-4ac9-fb15-c9529b59eff9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number:30.000000001\n",
            "30.000000001 \n",
            " x is greater than 30\n"
          ]
        }
      ],
      "source": [
        "x=float(input(\"enter a number:\"))\n",
        "match x:\n",
        "  case _ if x<=10:\n",
        "    print(x,\"\\n x is between 1-10\")\n",
        "  case _ if x<=20:\n",
        "    print(x,\"\\n x is betweeen 11-20\")\n",
        "  case _ if x<=30:\n",
        "    print(x,\"\\n x is between 21-30\")\n",
        "  case _ if x>=0:\n",
        "    print(x,\"\\n x is greater than 30\")\n"
      ]
    }
  ]
}