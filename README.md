# My First Repo

Hi, I'm **Andoni Rebollo**, a Mechanical Engineering student in the Honors College at Florida International University (FIU).

This is my first GitHub repository. I'm using it to learn Git and to keep track of projects as I build them.

## About me

- 🎓 Mechanical Engineering @ FIU (expected May 2029)
- 🌍 English, Spanish and Basque (learning Italian)
- 🤖 Interested in tech, AI and engineering
- 🧗 Climber

## Technical skills

- **Python:** engineering calculations and scripts
- **Git and GitHub:** version control, commits, pushing and pulling, GitHub CLI (`gh`)
- **Terminal (macOS):** Homebrew, command-line tools
- **Statics:** free body diagrams, reactions, cable forces

## Projects

### Golden Gate Bridge cable statics ([`golden_gate_statics.py`](golden_gate_statics.py))

Models the main span cable as a parabola under uniform load and computes the horizontal cable tension, tower reactions, maximum tension and cable stress, for dead load alone and with full live load. It uses published data from the Golden Gate Bridge District (span 4,200 ft, sag 470 ft, deck and cable weights, live load capacity).

Result: the total load on each tower comes out to about 61,100 tons with full live load, within 1% of the published 61,500 tons.

Run it:

```
python3 golden_gate_statics.py
```

## What I've learned so far

- Installing tools with Homebrew (`brew install gh`)
- Signing in to GitHub from the terminal (`gh auth login`)
- Creating a repo and pushing it (`git init`, `git add`, `git commit`, `gh repo create`)
- The everyday loop: edit, then `git add .`, `git commit -m "message"`, `git push`, and `git pull` to get changes made elsewhere
