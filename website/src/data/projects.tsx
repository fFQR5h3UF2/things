
import {sortBy} from '@site/src/utils/jsUtils';

export type TagType =
  // DO NOT USE THIS TAG: we choose sites to add to favorites
  | 'favorite'
  // For open-source sites, a link to the source code is required.
  // The source should be the *website's* source, not the project's source!
  | 'opensource'
  | 'product'
  // Feel free to add the 'design' tag as long as there's _some_ level of
  // CSS/swizzling.
  | 'design'
  // Site must have more than one locale.
  | 'i18n'
  | 'versioning'
  // Large sites are defined as those with > 200 pages, excluding versions.
  | 'large'
  | 'meta'
  | 'personal'
  // Right-to-left direction.
    | 'rtl';

const Projects: Project[] = [
  {
    title: 'AgileTs',
    description: 'Global State and Logic Framework for reactive Applications',
    preview: require('./showcase/agilets.png'),
    website: 'https://agile-ts.org/',
    source: 'https://github.com/agile-ts/documentation',
    tags: ['opensource', 'design'],
  },
  {
    title: 'AI-Speaker',
    description: 'Local, reliable, fast and private Audio and IoT gate.',
    preview: require('./showcase/aispeaker.png'),
    website: 'https://ai-speaker.com/',
    source: 'https://github.com/sviete/AIS-WWW',
    tags: ['opensource'],
    },
]

export type Project = {
  title: string;
  description: string;
  preview: string | null; // null = use our serverless screenshot service
  website: string;
  source: string | null;
  tags: TagType[];
};

export type Tag = {
  label: string;
  description: string;
  color: string;
};

export const Tags: {[type in TagType]: Tag} = {
  favorite: {
    label: "Favorite",
    description: "Our favorite Docusaurus sites that you must absolutely check out!",
    color: '#e9669e',
  },

  opensource: {
    label: "Open-Source",
    description: "Open-Source Docusaurus sites can be useful for inspiration!",
    color: '#39ca30',
  },

  product: {
    label: "Product",
    description: "Docusaurus sites associated to a commercial product!",
    color: '#dfd545',
  },

  design: {
    label: "Design",
    description: "Beautiful Docusaurus sites, polished and standing out from the initial template!",
    color: '#a44fb7',
  },

  i18n: {
    label: "I18n",
    description: "Translated Docusaurus sites using the internationalization support with more than 1 locale.",
    color: '#127f82',
  },

  versioning: {
    label: "Versioning",
    description: "Docusaurus sites using the versioning feature of the docs plugin to manage multiple versions.",
    color: '#fe6829',
  },

  large: {
    label: "Large",
    description: "Very large Docusaurus sites, including many more pages than the average!",
    color: '#8c2f00',
  },

  meta: {
    label: "Meta",
    description: "Docusaurus sites of Meta (formerly Facebook) projects",
    color: '#4267b2', // Facebook blue
  },

  personal: {
    label: "Personal",
    description: "Personal websites, blogs and digital gardens built with Docusaurus",
    color: '#14cfc3',
  },

  rtl: {
    label: "RTL Direction",
    description: "right to left",
    color: '#ffcfc3',
  },
};

export const TagList = Object.keys(Tags) as TagType[];
function sortProjects() {
  let result = Projects;
  // Sort by site name
  result = sortBy(result, (project: Project) => project.title.toLowerCase());
  // Sort by favorite tag, favorites first
  result = sortBy(result, (project: Project) => !project.tags.includes('favorite'));
  return result;
}

export const sortedProjects = sortProjects();
