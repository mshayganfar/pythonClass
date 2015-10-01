(deftemplate MENTAL-STATE::belief
"Robot's belief based on SharedPlans theory."
(slot turn (type STRING))
(slot id (type STRING))
(slot task (type STRING))
(slot event (type STRING))
(slot event-type (type SYMBOL) (allowed-values UTTERANCE ACTION EMOTION UNKNOWN) (default UNKNOWN))
(slot event-origin (type SYMBOL) (allowed-values EXTERNAL_EVENT INTERNAL_EVENT UNKNOWN) (default UNKNOWN))
(slot agent (type SYMBOL) (allowed-values ROBOT HUMAN UNKNOWN) (default UNKNOWN))
(slot belief-type (type SYMBOL) (allowed-values PRIVATE INFERRED MUTUAL UNKNOWN) (default UNKNOWN))
(slot belief-about (type SYMBOL) (allowed-values SELF OTHER ENVIRONMENT TASK UNKNOWN) (default UNKNOWN))
(slot belief (type STRING))
(slot strength (type SYMBOL) (allowed-values HIGH MEDIUM LOW UNKNOWN) (default UNKNOWN))
(slot accuracy (type SYMBOL) (allowed-values HIGH MEDIUM LOW UNKNOWN) (default UNKNOWN))
(slot frequency (type SYMBOL) (allowed-values HIGH MEDIUM LOW UNKNOWN) (default UNKNOWN))
(slot recency (type SYMBOL) (allowed-values HIGH MEDIUM LOW UNKNOWN) (default UNKNOWN))
(slot saliency (type SYMBOL) (allowed-values HIGH MEDIUM LOW UNKNOWN) (default UNKNOWN))
(slot persistence (type SYMBOL) (allowed-values HIGH MEDIUM LOW UNKNOWN) (default UNKNOWN)))