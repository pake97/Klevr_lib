# Get a training dataset

from pykeen.datasets import Nations
from pykeen.training import SLCWATrainingLoop
from torch.optim import Adam
from pykeen.evaluation import RankBasedEvaluator
from pykeen.models import TransE
from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
from pykeen.datasets.nations import NATIONS_TRAIN_PATH, NATIONS_TEST_PATH
#models=['CrossE', 'RotatE', 'TransE', 'TuckER', 'TorusE', 'TransH', 'TransR', 'TransD', 'TransF', 'RESCAL', 'NTN', 'HolE', 'DistMult', 'SimplE', 'ComplEx', 'ConvE', 'ConvKB']
models=['ConvE']

training = TriplesFactory.from_path(NATIONS_TRAIN_PATH)
testing = TriplesFactory.from_path(
    NATIONS_TEST_PATH,
    entity_to_id=training.entity_to_id,
    relation_to_id=training.relation_to_id,
)

""" dataset = Nations()
training_triples_factory = dataset.training

# Pick a model

model = TransE(triples_factory=training_triples_factory)

# Pick an optimizer from Torch

optimizer = Adam(params=model.get_grad_params())

# Pick a training approach (sLCWA or LCWA)

training_loop = SLCWATrainingLoop(
    model=model,
    triples_factory=training_triples_factory,
    optimizer=optimizer,
)

# Train like Cristiano Ronaldo
_ = training_loop.train(
    triples_factory=training_triples_factory,
    num_epochs=50,
    batch_size=256,
    
)

# Pick an evaluator

evaluator = RankBasedEvaluator()

# Get triples to test
mapped_triples = dataset.testing.mapped_triples

# Evaluate
results = evaluator.evaluate(
    model=model,
    mapped_triples=mapped_triples,
    batch_size=1024,
    additional_filter_triples=[
        dataset.training.mapped_triples,
        dataset.validation.mapped_triples,
    ],
)
print(results)
results.plot() """
for _model in models:
    toy_results = pipeline(
        training=training,
        testing=testing,
        model=_model,
        loss='softplus',
        model_kwargs=dict(embedding_dim=10),
        optimizer_kwargs=dict(lr=1.0e-1),
        training_kwargs=dict(num_epochs=128, use_tqdm_batch=False),
        evaluation_kwargs=dict(use_tqdm=False),
        random_seed=1,
        device='cpu',
    )
    toy_results.save_to_directory('embedding_models/nations_'+_model)
