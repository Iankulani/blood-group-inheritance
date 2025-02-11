# -*- coding: utf-8 -*-
"""
Created on Tue Feb  11 08:04:47 2024

@author: IAN CARTER KULANI
"""

import tkinter as tk
from tkinter import messagebox
import random

# Blood group inheritance simulation
class BloodGroupInheritance:
    def __init__(self, male_blood, female_blood):
        self.male_blood = male_blood
        self.female_blood = female_blood

    def get_possible_blood_groups(self):
        male_genotype = self.get_genotype(self.male_blood)
        female_genotype = self.get_genotype(self.female_blood)

        possible_blood_groups = []

        # Crossbreed and get the possible offspring's blood groups
        for male_allele in male_genotype:
            for female_allele in female_genotype:
                offspring_blood = male_allele + female_allele
                # Determine the blood group based on the alleles
                blood_group = self.get_blood_group(offspring_blood)
                if blood_group not in possible_blood_groups:
                    possible_blood_groups.append(blood_group)

        return possible_blood_groups

    def get_genotype(self, blood_group):
        # Return possible genotypes based on the blood group
        if blood_group == "A":
            return ["AA", "AO"]
        elif blood_group == "B":
            return ["BB", "BO"]
        elif blood_group == "AB":
            return ["AB"]
        elif blood_group == "O":
            return ["OO"]
        else:
            return []

    def get_blood_group(self, genotype):
        # Determine the blood group based on genotype
        if "A" in genotype and "B" in genotype:
            return "AB"
        elif "A" in genotype:
            return "A"
        elif "B" in genotype:
            return "B"
        elif "O" in genotype:
            return "O"
        else:
            return "Unknown"

# GUI class
class BloodGroupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Group Inheritance Simulation")
        self.root.geometry("600x400")
        self.root.config(bg='lightblue')

        # Title label
        self.title_label = tk.Label(self.root, text="Blood Group Inheritance Simulator", bg="lightblue", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Male Blood Group input
        self.male_label = tk.Label(self.root, text="Enter Male Blood Group (A, B, AB, O)", bg="lightblue")
        self.male_label.pack()

        self.male_entry = tk.Entry(self.root)
        self.male_entry.pack()

        # Female Blood Group input
        self.female_label = tk.Label(self.root, text="Enter Female Blood Group (A, B, AB, O)", bg="lightblue")
        self.female_label.pack()

        self.female_entry = tk.Entry(self.root)
        self.female_entry.pack()

        # Button to simulate
        self.simulate_button = tk.Button(self.root, text="Simulate Blood Group", command=self.simulate_inheritance)
        self.simulate_button.pack(pady=20)

        # Results label
        self.results_label = tk.Label(self.root, text="", bg="lightblue", font=("Helvetica", 12))
        self.results_label.pack(pady=10)

    def simulate_inheritance(self):
        male_blood = self.male_entry.get().upper()
        female_blood = self.female_entry.get().upper()

        # Validate input
        if male_blood not in ["A", "B", "AB", "O"] or female_blood not in ["A", "B", "AB", "O"]:
            messagebox.showerror("Input Error", "Please enter valid blood groups: A, B, AB, or O.")
            return

        # Initialize the inheritance simulation
        inheritance = BloodGroupInheritance(male_blood, female_blood)
        possible_blood_groups = inheritance.get_possible_blood_groups()

        # Display the results
        self.results_label.config(text=f"Possible Blood Groups for Offspring: {', '.join(possible_blood_groups)}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BloodGroupApp(root)
    root.mainloop()
