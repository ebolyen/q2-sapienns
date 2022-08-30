import pandas as pd

from qiime2.plugin.testing import TestPluginBase

from q2_sapienns import HumannGeneFamilyFormat
from q2_sapienns._humann import humann_genefamily

class HumannTests(TestPluginBase):

    package = 'q2_sapienns.tests'

    def test_humann_genefamilies(self):
        _, input_table_df =  self.transform_format(
            HumannGeneFamilyFormat, pd.DataFrame, 'humann-genefamilies-1.tsv'
        )

        obs_table, obs_tax = humann_genefamily(input_table_df)

        # Assess resulting tables
        self.assertEqual(obs_table.index.name, 'sample-id')
        self.assertEqual(obs_table.shape, (1, 12))
        self.assertEqual(list(obs_table.index), ['sample1'])
        self.assertEqual(
            list(obs_table.columns),
            ['UNMAPPED', 'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
            ])

        self.assertEqual(list(obs_table.T['sample1']),
                         [187.0, 150.0, 150.0, 67.0, 57.0, 5.0, 4.0,
                          1.0, 60.0, 31.0, 22.0, 7.0])

        # Assess resulting feature metadata
        self.assertEqual(obs_tax.index.name, 'Feature ID')
        self.assertEqual(obs_tax.shape, (12, 1))
        self.assertEqual(list(obs_tax.columns), ['Taxon'])
        self.assertEqual(
            list(obs_tax.index),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
            ])

        self.assertEqual(
            list(obs_tax['Taxon']),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_stercoris',
            ])

    def test_humann_genefamilies_unchanged_sample_ids(self):
        _, input_table_df =  self.transform_format(
            HumannGeneFamilyFormat, pd.DataFrame, 'humann-genefamilies-1.tsv'
        )

        obs_table, obs_tax = humann_genefamily(
            input_table_df, strip_units_from_sample_ids=False)

        # Assess resulting tables
        self.assertEqual(obs_table.index.name, 'sample-id')
        self.assertEqual(obs_table.shape, (1, 12))
        self.assertEqual(list(obs_table.index), ['sample1_Abundance-RPKs'])
        self.assertEqual(
            list(obs_table.columns),
            ['UNMAPPED', 'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
            ])

        self.assertEqual(list(obs_table.T['sample1_Abundance-RPKs']),
                         [187.0, 150.0, 150.0, 67.0, 57.0, 5.0, 4.0,
                          1.0, 60.0, 31.0, 22.0, 7.0])

        # Assess resulting feature metadata
        self.assertEqual(obs_tax.index.name, 'Feature ID')
        self.assertEqual(obs_tax.shape, (12, 1))
        self.assertEqual(list(obs_tax.columns), ['Taxon'])
        self.assertEqual(
            list(obs_tax.index),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
            ])

        self.assertEqual(
            list(obs_tax['Taxon']),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_stercoris',
            ])

    def test_humann_genefamilies_multi_sample(self):
        _, input_table_df =  self.transform_format(
            HumannGeneFamilyFormat, pd.DataFrame, 'humann-genefamilies-2.tsv'
        )

        obs_table, obs_tax = humann_genefamily(input_table_df)

        # Assess resulting tables
        self.assertEqual(obs_table.index.name, 'sample-id')
        self.assertEqual(obs_table.shape, (2, 14))
        self.assertEqual(list(obs_table.index), ['sample1', 'sample_2'])
        self.assertEqual(
            list(obs_table.columns),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|unclassified',
            ])

        self.assertEqual(list(obs_table.T['sample1']),
                         [187.0, 150.0, 150.0, 25.0, 67.0, 57.0, 5.0, 4.0,
                          1.0, 60.0, 31.0, 22.0, 7.0, 0.0])

        self.assertEqual(list(obs_table.T['sample_2']),
                         [42.0, 50.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          45.0, 40.0, 2.0, 2.0, 1.0])

        # Assess resulting feature metadata
        self.assertEqual(obs_tax.index.name, 'Feature ID')
        self.assertEqual(obs_tax.shape, (14, 1))
        self.assertEqual(list(obs_tax.columns), ['Taxon'])
        self.assertEqual(
            list(obs_tax.index),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|unclassified',
            ])

        self.assertEqual(
            list(obs_tax['Taxon']),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_unknown; g__Bacteroides; s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_stercoris',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; unclassified',
            ])

    def test_humann_genefamilies_multi_sample_unchanged_sample_ids(self):
        _, input_table_df =  self.transform_format(
            HumannGeneFamilyFormat, pd.DataFrame, 'humann-genefamilies-2.tsv'
        )

        obs_table, obs_tax = humann_genefamily(
            input_table_df, strip_units_from_sample_ids=False
        )

        # Assess resulting tables
        self.assertEqual(obs_table.index.name, 'sample-id')
        self.assertEqual(obs_table.shape, (2, 14))
        self.assertEqual(list(obs_table.index),
                         ['sample1_Abundance-RPKs', 'sample_2_Abundance-RPKs'])
        self.assertEqual(
            list(obs_table.columns),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|unclassified',
            ])

        self.assertEqual(list(obs_table.T['sample1_Abundance-RPKs']),
                         [187.0, 150.0, 150.0, 25.0, 67.0, 57.0, 5.0, 4.0,
                          1.0, 60.0, 31.0, 22.0, 7.0, 0.0])

        self.assertEqual(list(obs_table.T['sample_2_Abundance-RPKs']),
                         [42.0, 50.0, 0.0, 25.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                          45.0, 40.0, 2.0, 2.0, 1.0])

        # Assess resulting feature metadata
        self.assertEqual(obs_tax.index.name, 'Feature ID')
        self.assertEqual(obs_tax.shape, (14, 1))
        self.assertEqual(list(obs_tax.columns), ['Taxon'])
        self.assertEqual(
            list(obs_tax.index),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_unknown|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon|unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|g__Bacteroides.s__Bacteroides_stercoris',
             'UniRef50_O83668: Fructose-bisphosphate aldolase|unclassified',
            ])

        self.assertEqual(
            list(obs_tax['Taxon']),
            ['UNMAPPED',
             'UniRef50_unknown',
             'UniRef50_unknown; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_unknown; g__Bacteroides; s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_fragilis',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_finegoldii',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; g__Bacteroides; s__Bacteroides_stercoris',
             'UniRef50_A6L0N6: Conserved protein found in conjugate transposon; unclassified',
             'UniRef50_O83668: Fructose-bisphosphate aldolase',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_vulgatus',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_thetaiotaomicron',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; g__Bacteroides; s__Bacteroides_stercoris',
             'UniRef50_O83668: Fructose-bisphosphate aldolase; unclassified',
            ])
