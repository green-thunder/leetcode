from utils.updater import SolutionUpdater

new_solutions = [
    {
        "index": 1,
        "language": "python",
        "title": "Two Sum",
        "difficulty": "easy",
        "link": "https://leetcode.com/problems/two-sum/"
    }
]

readme_path = "README.md"
solution_updater = SolutionUpdater(readme_path)
solution_updater.update_or_add_solutions(new_solutions)
