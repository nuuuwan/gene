class GeneConsoleRunnerReadConfigs:
    def getReadCommandConfigNavigation(self):
        return [
            dict(
                cmd1_list=['cd', 'find', 'search'],
                func=self.search,
                description='find person',
                has_after=True,
            ),
            dict(
                cmd1_list=['previous', 'p'],
                func=self.prev,
                description="goto previous person",
            ),
            dict(
                cmd1_list=['his', 'history'],
                func=self.history,
                description="list person history",
            ),
            dict(
                cmd1_list=['r', 'rand', 'random'],
                func=self.random,
                description="list a random person",
            ),
        ]

    def getReadCommandConfigNavigationFamily(self):
        return [
            dict(
                cmd1_list=['father', 'f'],
                func=lambda: self.goto(self.current_person.father_id),
                description="goto the current person's father",
            ),
            dict(
                cmd1_list=['mother', 'm'],
                func=lambda: self.goto(self.current_person.mother_id),
                description="goto the current person's mother",
            ),
            dict(
                cmd1_list=['spouse', 'x', 'w', 'h'],
                func=self.spouse,
                description="list the current persons [num]th spouse",
                has_after=True,
            ),
            dict(
                cmd1_list=['child', 'c', 's', 'd'],
                func=self.child,
                description="list the current persons [num]th child ",
                has_after=True,
            ),
        ]

    def getReadCommandConfigVisualization(self):
        return [
            dict(
                cmd1_list=['v', 'ls', 'vis'],
                func=self.vis,
                description="visualize current person",
            ),
            dict(
                cmd1_list=['vd', 'vis_des'],
                func=self.vis_des,
                description="visualize current person's descendants",
            ),
            dict(
                cmd1_list=['va', 'vis_anc'],
                func=self.vis_anc,
                description="visualize current person's ancestors",
            ),
            dict(
                cmd1_list=['vea', 'vis_end_anc'],
                func=self.vis_end_anc,
                description="visualize current person's"
                + " end ancestors (those without ancestors)",
            ),
            dict(
                cmd1_list=['rel'],
                func=self.vis_rel,
                description="visualize current person's relatives",
            ),
        ]

    def getReadCommandConfigValidation(self):
        return [
            dict(
                cmd1_list=['singletons', 'sin'],
                func=self.vis_singletons,
                description="visualize singletons"
                + " (people without relatives)",
            ),
            dict(
                cmd1_list=['similar_pairs', 'similar', 'sim'],
                func=self.vis_similar_pairs,
                description="visualize similar pairs "
                + "(Pairs of people who might be the same person)",
            ),
            dict(
                cmd1_list=['birthdate', 'bd'],
                func=self.birthdate,
                description="print or estimate the current person's birthdate",
            ),
            dict(
                cmd1_list=['compare'],
                func=self.compare,
                description="Compare the current person to person with [id]",
                has_after=True,
            ),
        ]

    def getReadCommandConfigReference(self):
        return [
            dict(
                cmd1_list=['google', 'goo'],
                func=self.current_person.google,
                description="Search for the current person on Google",
            ),
            dict(
                cmd1_list=['facebook', 'fb'],
                func=self.current_person.facebook,
                description="Search for the current person on Facebook",
            ),
            dict(
                cmd1_list=['linkedin', 'li'],
                func=self.current_person.linkedin,
                description="Search for the current person on LinkedIn",
            ),
            dict(
                cmd1_list=['www'],
                func=self.current_person.www,
                description="Search for the current person on the internet",
            ),
        ]

    def getReadCommandConfig(self):
        return (
            self.getReadCommandConfigNavigation()
            + self.getReadCommandConfigNavigationFamily()
            + self.getReadCommandConfigReference()
            + self.getReadCommandConfigVisualization()
            + self.getReadCommandConfigValidation()
        )
