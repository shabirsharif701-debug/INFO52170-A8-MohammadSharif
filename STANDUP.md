# Daily Standup Log

| Date | Member | What I did | What I will do | Blockers |
|---|---|---|---|---|
| **Sprint 1** | | | | |
| 2026-08-14 | Mohammad Sharif | Set up repo, Flask skeleton, EC2 instance, Product Backlog board | Build CI/CD pipeline (GitHub Actions) | None |
| 2026-08-14 | Mohammad Sharif | Built `.github/workflows/ci.yml` with lint + test stages, opened PR | Fix flake8 formatting errors causing pipeline failure | Pipeline failing on lint step |
| 2026-08-14 | Mohammad Sharif | Fixed flake8 issues, corrected ci.yml content, moved test_app.py to repo root | Confirm pipeline passes on main, close out CI/CD issue | None |
| **Sprint 2** | | | | |
| 2026-08-15 | Mohammad Sharif | Verified EC2 instance after Learner Lab restart, installed Docker (dnf) on Amazon Linux 2023, wrote Dockerfile on feature/dockerize-app | Build and run the Docker image on EC2 | None |
| 2026-08-15 | Mohammad Sharif | Built flask-app image, ran container (port 80→5000), confirmed app in browser via public IP | Merge Docker branch to main, check security group config | None |
| 2026-08-15 | Mohammad Sharif | Merged feature/dockerize-app to main (--no-ff), confirmed security group allows only HTTP:80 and SSH:22 | Complete standup log, sprint reviews, and retrospectives | None |