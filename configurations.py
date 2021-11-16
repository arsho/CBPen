from utils import is_url_available, print_on_console


def get_vm_urls():
    default_machine = "http://127.0.0.1:5000"
    virtual_machines = [
        "http://ec2-18-191-54-92.us-east-2.compute.amazonaws.com",
        "http://ec2-3-131-94-210.us-east-2.compute.amazonaws.com",
        "http://ec2-3-139-90-249.us-east-2.compute.amazonaws.com"
    ]
    for i in range(len(virtual_machines)):
        if not is_url_available(virtual_machines[i]):
            virtual_machines[i] = default_machine
    print_on_console("Virtual machines after the scan", "virtual machines", virtual_machines)
    return virtual_machines


def get_allowed_sites():
    return ["localhost", "scanme.nmap.org", "example.com",
            "example.net", "example.org", "webscantest.com"]


def get_scan_types():
    return [
        ["ports", "Port Scan"],
        ["services", "Services and operating systems"],
        ["subdomains", "Subdomains and SSL certificates"]
    ]


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
