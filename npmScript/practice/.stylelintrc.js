module.exports={
  "plugins": [
     "stylelint-scss"
  ],
  "extends": [
    "stylelint-config-recommended",
    "stylelint-config-recommended-scss"
  ],
  "rules": {
    "at-rule-no-unknown": [
      true,
      {
        "ignoreAtRules": [
          "extends",
          "ignores"
        ]
      }
    ],
    "block-no-empty": null,
    "number-leading-zero": null,
    "unit-whitelist": [
      "em",
      "rem",
      "s",
      "%",
      "px"
    ]
  }
};
