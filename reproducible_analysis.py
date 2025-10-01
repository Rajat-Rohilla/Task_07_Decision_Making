#!/usr/bin/env python3
"""Minimal reproducible script for quick replication."""
import numpy as np
games = ['Tennessee', 'UConn', 'Colgate', 'Clemson', 'Duke']
team_pts = [26, 27, 66, 34, 3]
opp_pts = [45, 20, 24, 21, 38]
team_pts = np.array(team_pts)
opp_pts = np.array(opp_pts)
print('Team PPG', team_pts.mean())
print('Opp PPG', opp_pts.mean())
