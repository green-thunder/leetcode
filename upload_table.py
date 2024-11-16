from utils.updater import SolutionUpdater

new_solutions = [
    {
        "index": 3,
        "language": "java",
        "title": "Two Sum",
        "difficulty": "easy",
        "slug": "two-sum"
    }
]

readme_path = "README.md"
solution_updater = SolutionUpdater(readme_path)
solution_updater.update_or_add_solutions(new_solutions)
