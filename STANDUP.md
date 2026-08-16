# Daily Standup Log

| Date | Member | What I did | What I will do | Blockers |
|---|---|---|---|---|
| **Sprint 1** | | | | |
| 2026-08-03 | Mohammad Sharif | Set up repo, Flask skeleton, EC2 instance, Product Backlog board | Build CI/CD pipeline (GitHub Actions) | None |
| 2026-08-05 | Mohammad Sharif | Built `.github/workflows/ci.yml` with lint + test stages, opened PR | Fix flake8 formatting errors causing pipeline failure | Pipeline failing on lint step |
| 2026-08-07 | Mohammad Sharif | Fixed flake8 issues, corrected ci.yml content, moved test_app.py to repo root, pipeline passing on main | Sprint 1 review, plan Sprint 2 backlog | None |
| **Sprint 2** | | | | |
| 2026-08-10 | Mohammad Sharif | Sprint 2 planning: selected Docker containerization and AWS deployment stories | Install Docker and write Dockerfile | None |
| 2026-08-14 | Mohammad Sharif | Verified EC2 instance after Learner Lab restart, installed Docker (dnf) on Amazon Linux 2023, wrote Dockerfile on feature/dockerize-app | Build and run the Docker image on EC2 | None |
| 2026-08-15 | Mohammad Sharif | Built flask-app image, ran container (port 80→5000), confirmed app in browser via public IP; merged feature/dockerize-app to main (--no-ff) | Confirm security group config, complete AWS deployment | None |
| 2026-08-16 | Mohammad Sharif | Confirmed security group allows only HTTP:80 and SSH:22; completed standup log, sprint reviews, and retrospectives | Prepare final presentation (Week 14) | None |