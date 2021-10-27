def get_allowed_sites():
    return ["localhost", "scanme.nmap.org", "example.com"]


def get_contributors():
    return {
        "advisors": [
            {
                "name": "Ragib Hasan",
                "designation": "Associate Professor",
                "department": "Computer Science",
                "work_place": "University of Alabama at Birmingham"
            }
        ],
        "members": [
            {
                "name": "Ahmedur Rahman Shovon",
                "blazer_id": "ashovon"
            },
            {
                "name": "Andrew Balfour",
                "blazer_id": "abalfour"
            },
            {
                "name": "Jeremy Crown",
                "blazer_id": "jrcrown"
            },
            {
                "name": "Trina Lin",
                "blazer_id": "trinal00"
            },
            {
                "name": "William Austin",
                "blazer_id": "jemar"
            }
        ]
    }


def get_terms():
    terms = [
        "CBPen is created to practice cloud security best practices. Cloud blazers is not responsible for any of the misuse of this tool.",
        "CBPen cannot be used for commercial purposes.",
        "A conscent from the CBPen group members is necessary to copy any of the content of the project."
    ]
    return terms


def get_policies():
    policies = [
        "CBPen is created to practice cloud security best practices. Cloud blazers is not responsible for any of the misuse of this tool.",
        "CBPen cannot be used for commercial purposes.",
        "A conscent from the CBPen group members is necessary to copy any of the content of the project."
    ]
    return policies
