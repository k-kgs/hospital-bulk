_batches = {}

def save_batch(batch):
    _batches[batch.batch_id] = batch

def get_batch(batch_id):
    return _batches.get(batch_id)
