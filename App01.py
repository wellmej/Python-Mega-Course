{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#-----------------------------------------------------\n",
    "#  Add Fuzzy search logic to the function\n",
    "#-----------------------------------------------------\n",
    "def search_word_fuzzy(word_in, dictionary_in):\n",
    "    word_in = word_in.lower()\n",
    "    if word_in in dictionary_in:\n",
    "        definition = dictionary_in[word_in]\n",
    "        return definition\n",
    "    elif len(get_close_matches(word_in, dictionary_in.keys(), cutoff = 0.8, n = 3)) > 0:\n",
    "        close_word = get_close_matches(word_in, dictionary_in.keys())[0]\n",
    "        definition = 'Did you mean (' + close_word + ') instead of ' + word +'?  Enter Y if yes, N if no'\n",
    "#       definition = 'Did you mean %s instead?' % close_word\n",
    "        yn = input (definition)\n",
    "        yn = yn.upper()\n",
    "        if yn == 'Y':\n",
    "            definition = dictionary_in[close_word]\n",
    "            return definition\n",
    "        elif yn == 'N':\n",
    "            definition = 'This word (' + word_in + ') was not found in the supplied dictionary. Please re-enter'\n",
    "            return definition\n",
    "        else:\n",
    "            definition = 'Please enter either Y or N. Please re-enter'\n",
    "            return definition\n",
    "    else:\n",
    "        definition = 'This word (' + word_in + ') was not found in the supplied dictionary. Please re-enter'\n",
    "        return definition\n",
    "    \n",
    "word = input(\"Enter Word: \")\n",
    "print(search_word_fuzzy(word,data))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
