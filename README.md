[![Build Status](https://travis-ci.org/logileifs/guid.svg?branch=master)](https://travis-ci.org/logileifs/guid)

# guid
Human friendly GUID/UUID library

# Install
`pip install guid`

# Usage
```python
>>> from guid import GUID
>>> guid = GUID()
>>> guid
'Kj2hvuO5Ra-VU5ghIJVnlQ'
>>> from guid import guid_to_uuid
>>> guid_to_uuid(guid)
UUID('2a3da1be-e3b9-45af-9553-982120956795')
>>> from guid import uuid_to_guid
>>> from uuid import uuid4
>>> u = uuid4()
>>> u
UUID('929f9121-8264-472a-a4ee-ff7557457f12')
>>> uuid_to_guid(u)
'kp-RIYJkRyqk7v91V0V_Eg'
>>> guid_to_uuid('kp-RIYJkRyqk7v91V0V_Eg')
UUID('929f9121-8264-472a-a4ee-ff7557457f12')
```
