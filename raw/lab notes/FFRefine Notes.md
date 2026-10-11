
FFrefine is currently in a very promising stage, I have basically shown that you can use it to refine force field parameters. I have solid evidence that we can start from the Garnet water model and get to one with the correct RDF, decent density (given the 3-point water model) and correct dielectric. All of this, for a temperature ladder. 

I still need to do several things before it being in a publishable state, but I should probably start drafting a manuscript, since the introduction and most of the methods should not change anymore.

# What I need to do

- Clean up the code
- Turn FFRefine into an actual Julia package
- Decide what is going to be the final architecture for FFRefine:
	- What gradient aggregation method to use? I have ConFIG and weighted sum as of now. The latter is proving to be quite an annoyance. A family that becomes optimised can get a very small and noisy gradient that will mess up the whole ConFIG projection. For that I have implemented gating mechanisms, but this still feels a bit to ad-hoc, even though I tried to make them as principled as possible. If weighted sum gives decent results I might just stick with it.
	- We will use the Damped Fisher treatment as metric tensor, remove the other choices.
	- Explore if we can implement momentum with the damped fisher treatment. Momentum can be also problematic with some stability gates. I know this is specially difficult when using ConFIG... another reason to get rid of it maybe?
	- More...?
- Make FFRefine work with the master branch of Molly. This is probably going to be quite painful...
- Run FFRefine with the ethanol solvation experiment.
- In fact, I should think how to properly set up the experiments. I am thinking of a temperature ladder for water and a temperature ladder for ethanol. See where those parameters go. Then, run a solvation free energy experiment with the original garnet parameters for water and ethanol, and use FFRefine to fit that. Then, same experiment but using the temperature-ladder-refined parameters, see if the solvation free energy has improved just by that. The solvation free energies can also fit for things like RDF, density and dielectric, but just at one temperature.
- I need to look for quality experimental data for ethanol. RDF, density and dielectric, at different temperatures.

# What can be done now

Work on a draft for a manuscript. I can write the introduction and lay down at least the basic skeleton of the methods section. Methods in the paper should be concise and clear. Do not put derivations there, those go in the supporting materials. I can also lay down the basic framework of the results, when I clearly decide which experiments will I run.