Frontend
--------

Frontend implementation is so easy

you just need to add stream url as ``src`` in ``video`` tag

.. code:: html

    <video width="480" controls>
        <source src="http://localhost:8000/api/stream/?path=<path_to_video>" type="video/mp4">
    </video>