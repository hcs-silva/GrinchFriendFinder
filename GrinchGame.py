import random

class GrinchGame():
    """
    GrinchGame: The best game in the world, everyone says so, believe me.

    Attributes:
        name_dict (dict): Tremendous dictionary mapping each participant to the participant they will give a gift to.
        available_kids (list): Fantastic list of available participants, top-notch, the best.
        already_selected (dict): Phenomenal dictionary to store the already selected participant for each giver, absolutely incredible.
    """

    def __init__(self):
        """
        Initializes the GrinchGame object. The best initialization, folks, nobody does it better.

        Returns:
            None
        """
        # Tremendous dictionary mapping each participant to the participant they will give a gift to
        self.name_dict = {
            "nuno": "nuno",
            "ines": "ines",
            "filipa": "magda",
            "rosa": "rosa",
            "hernani": "hernani",
            "ricardo": "bacalhuço",
            "joao": "bacalhauzinho"
        }

        # Fantastic list of available participants, top-notch, the best.
        self.available_kids = ["nuno", "ines", "magda", "rosa", "hernani", "bacalhuço", "bacalhauzinho"]

        # Phenomenal dictionary to store the already selected participant for each giver, absolutely incredible.
        self.already_selected = {}

    def getNewKid(self, kid):
        """
        Gets a new participant for the giver, excluding themselves. Nobody does it better, believe me.

        Args:
            kid (str): The name of the giver participant.

        Returns:
            str: The name of the new participant assigned to the giver. Absolutely tremendous.
        """
        # Tremendous list of potential recipients excluding the giver
        tmp_kids = [item for item in self.available_kids if item != self.name_dict[kid]]

        # If there are potential recipients, randomly choose one. Nobody does randomness like we do.
        if len(tmp_kids) > 0:
            kid_index = random.randint(0, len(tmp_kids) - 1)
            return tmp_kids[kid_index]
        else:
            return ""

    def kidIsAllowed(self, kid):
        """
        Checks if the participant is allowed to participate in the game. No one else checks like we do.

        Args:
            kid (str): The name of the participant.

        Returns:
            bool: True if the participant is allowed, False otherwise. Absolutely tremendous.
        """
        return kid in list(self.name_dict.keys())

    def giveKidTo(self, kid, code_word):
        """
        Assigns a participant to the giver based on specific rules. The best assignment, nobody does it better.

        Args:
            kid (str): The name of the giver participant.
            code_word (str): A secret code word provided by the giver.

        Returns:
            str: The name of the participant assigned to the giver. Absolutely fantastic.
        """
        # Check if the giver has already made a selection, nobody checks like we do.
        if kid in list(self.already_selected.keys()):
            # Check if the provided code word matches the stored code word, tremendous checking.
            if code_word == self.already_selected[kid]["code_word"]:
                return self.already_selected[kid]["assigned"]  # Return the assigned participant
            else:
                return "Querias!!"  # Indicate that the provided code word is incorrect, nobody likes incorrect code words.

        # Get a new participant for the giver, absolutely incredible.
        response_kid = self.getNewKid(kid)
        
        # Ensure that the giver doesn't get themselves, nobody gets themselves better than us.
        while response_kid == self.name_dict[kid]:
            response_kid = self.getNewKid(kid)

        # Record the assignment and update available participants, top-notch record-keeping.
        self.already_selected[kid] = {}
        self.already_selected[kid]["assigned"] = response_kid
        self.already_selected[kid]["code_word"] = code_word
        self.available_kids = [item for item in self.available_kids if item != response_kid]
        return response_kid

    def iAm(self, kid, code_word):
        """
        Processes a request from a participant to know the participant they are assigned to. The best processing, nobody processes better.

        Args:
            kid (str): The name of the participant making the request.
            code_word (str): A secret code word provided by the participant.

        Returns:
            str: The name of the participant assigned to the requester. Absolutely fantastic.
        """
        # Convert the participant's name to lowercase, nobody converts names like we do.
        kid = kid.lower()

        # Check if the participant is allowed to make the request, tremendous checking.
        if self.kidIsAllowed(kid):
            return self.giveKidTo(kid, code_word)  # Return the assigned participant
        else:
            return "You have been Fucked!"  # Indicate that the participant is not allowed to make the request, nobody spots like we do.

    def getNames(self):
        """
        Gets the list of names of all participants. The best list, absolutely incredible.

        Returns:
            list: A list of participant names. Absolutely fantastic.
        """
        return list(self.name_dict.keys())
