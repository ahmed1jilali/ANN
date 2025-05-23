Evaluation du gradient par la rétropropagation
L’évaluation du gradient de la fonction de coût peut être effectuée à l’aide d’un algorithme de
rétropropagation [17], qui n’est pas un algorithme d’apprentissage, mais un ingrédient dans une
procédure d’apprentissage.
Considérant un réseau de neurones non bouclé avec des neurones cachés et un neurone de
sortie. L’extension à un réseau qui possède plusieurs neurones de sortie est triviale. Rappelons que
le neurone i calcule une quantité y_{i} qui est une fonction non linéaire de son potentiel v_{i}:

$$
y_{i} = f(v_{i}) = f(\sum_{j=1}^{n_{i}}w_{ij}x_{j}^{i})
$$

Où x_{j}^{i} désigne la variable j du neurone i. Les variables du neurone i peuvent être soit les sorties d’autres neurones, soit les variables du réseau.

La fonction de coût dont on cherche à évaluer le gradient est de la forme (3.17).

$$
J(w) = \sum_{k=1}^{N}(y_{k}^{p}-g(x_{k},w))^2 = \sum_{k=1}^{N} \pi(x_{k}, w)
$$

Où \pi(x_{k}, w) est la fonction de perte relative à l’exemple k.

y_{k}^{p}: est la sortie désirée de l’exemple k.

g(x_{k}, w): est la sortie estimée de l’exemple k.

L’algorithme de rétropropagation consiste essentiellement en l’application répétée de la règle
des dérivées composées. On remarque tout d’abord que la fonction de perte ne dépend du paramètre w_{ij} que par l’intermédiaire de la valeur de la sortie du neurone i , qui est elle-même fonction uniquement du potentiel du neurone i; on peut donc écrire :
